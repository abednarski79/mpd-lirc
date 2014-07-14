package eu.appbucket.beaconmonitor.core.service;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import uk.co.alt236.bluetoothlelib.device.BluetoothLeDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Parcelable;
import android.util.Log;
import eu.appbucket.beaconmonitor.core.constants.App;

public class CommunicationService extends BroadcastReceiver {
	
	private static final String LOG_TAG = CommunicationService.class.getName();
	private Context contex;
	
	@Override
	public void onReceive(Context context, Intent intent) {
		this.contex = context;
		Parcelable[] foundDevices = intent.getParcelableArrayExtra(App.BROADCAST_DEVICE_FOUND_PAYLOAD);
		for(Parcelable device:  foundDevices) {		
			reportStolenAsset((BluetoothLeDevice) device);
		}
	}
	
	public void reportStolenAsset(BluetoothLeDevice device) {
		if(!isOnline()) {
			log("Connection is not available");
			return;
		}		
	}
	
	public boolean isOnline() {
	    ConnectivityManager connMgr = (ConnectivityManager) contex.getSystemService(Context.CONNECTIVITY_SERVICE);
	    NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
	    return (networkInfo != null && networkInfo.isConnected());
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
