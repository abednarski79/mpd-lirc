package eu.appbucket.beaconmonitor.core.service;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Serializable;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import org.json.JSONException;
import org.json.JSONObject;

import uk.co.alt236.bluetoothlelib.device.BluetoothLeDevice;
import uk.co.alt236.bluetoothlelib.device.mfdata.IBeaconManufacturerData;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.location.Location;
import android.location.LocationManager;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Parcelable;
import android.util.Log;
import eu.appbucket.beaconmonitor.core.constants.App;

public class CommunicationService extends BroadcastReceiver {
	
	private static final String LOG_TAG = CommunicationService.class.getName();
	private Context context;

	private class StolenAsset implements Serializable {
		
		private String assetId;
		private double latitude;
		private double longitude;
		
		public StolenAsset(BluetoothLeDevice beacon, Location location) {
			IBeaconManufacturerData iBeaconData = new IBeaconManufacturerData(beacon);
			this.assetId = iBeaconData.getUUID();
			this.longitude = location.getLongitude();
			this.latitude = location.getLatitude();
		}
		
		public String getAssetId() {
			return assetId;
		}
		public void setAssetId(String assetId) {
			this.assetId = assetId;
		}
		public double getLatitude() {
			return latitude;
		}
		public void setLatitude(double latitude) {
			this.latitude = latitude;
		}
		public double getLongitude() {
			return longitude;
		}
		public void setLongitude(double longitude) {
			this.longitude = longitude;
		}
		
		public String toJson() throws JSONException {
			JSONObject jsonObj = new JSONObject();
			jsonObj.put("assetId", this.assetId);
			jsonObj.put("latitude", this.latitude);
			jsonObj.put("longitude", this.longitude);			
			return jsonObj.toString();
		}
	}
	
	@Override
	public void onReceive(Context context, Intent intent) {
		this.context = context;
		Parcelable[] foundDevices = intent.getParcelableArrayExtra(App.BROADCAST_DEVICE_FOUND_PAYLOAD);
		for(Parcelable device:  foundDevices) {		
			try {
				reportStolenAsset((BluetoothLeDevice) device);
			} catch (JSONException e) {
				log("Can't convert to json");
			}
		}
	}
	
	public void reportStolenAsset(BluetoothLeDevice device) throws JSONException {
		if(!isOnline()) {
			log("Connection is not available");
			return;
		}
		Location currentLocation = getCurrentLocation();
		StolenAsset stolenAsset = new StolenAsset(device, currentLocation);
		String jsonRepresentation = stolenAsset.toJson();
		String reportUrl = "http://api.dev.bicycle.appbucket.eu/reports";
		try {
			URL url = new URL(reportUrl);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setReadTimeout(10000 /* milliseconds */);
	        conn.setConnectTimeout(15000 /* milliseconds */);
	        conn.setRequestMethod("POST");
	        conn.setDoInput(true);
	        OutputStreamWriter wr= new OutputStreamWriter(conn.getOutputStream());
	        wr.write(jsonRepresentation);
	        wr.flush();
	        int HttpResult =conn.getResponseCode();
	        if(HttpResult == HttpURLConnection.HTTP_OK){
	        	log("Data sent successfully.");
	        } else {
	        	log("Connection failed: " + HttpResult);
	        }	        
		} catch (MalformedURLException e) {
			log("Can't convert to url: " + reportUrl);
		} catch (IOException e) {
			log("Can't establish connection to url: " + reportUrl);
		}
		
		
	}
	
	private boolean isOnline() {
	    ConnectivityManager connMgr = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
	    NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
	    return (networkInfo != null && networkInfo.isConnected());
	}  
	
	private Location getCurrentLocation() {
		LocationManager locationManager = (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);
		return locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
	}
	
	public UUID[] getStoleAssets() {
		List<UUID> stoleAssets = new ArrayList<UUID>();
		stoleAssets.add(UUID.fromString("F4C36EAC-0767-11E4-A4ED-B2227CCE2B54"));
		UUID[] stolenUUIDs = new UUID[stoleAssets.size()];
		stoleAssets.toArray(stolenUUIDs);
		return stolenUUIDs;
	}	
	
	private void log(String log) {
		Log.d(LOG_TAG, log);
	}
}
