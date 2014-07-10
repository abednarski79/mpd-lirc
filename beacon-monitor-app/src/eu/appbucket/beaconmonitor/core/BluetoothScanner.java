package eu.appbucket.beaconmonitor.core;

import java.util.ArrayList;
import java.util.List;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothAdapter.LeScanCallback;
import android.bluetooth.BluetoothManager;
import android.content.Context;
import android.os.Handler;
import android.util.Log;

public class BluetoothScanner {
	
	public BluetoothScanner(Context context) {
		this.context = context;
	}
	
	private Context context;
	
	// private List<String> foundDevices = new ArrayList<String>();
	
	private static final String LOG_TAG = BluetoothScanner.class.getName();
	
	private BluetoothAdapter bluetoothAdapter;
	
	private ServerService serverService = new ServerService();
	
	private LeScanCallback bluetoothCallback = new LeScanCallback() {
		
		private ServerService serverService = new ServerService();
		
		public void onLeScan(android.bluetooth.BluetoothDevice device, int rssi, byte[] scanRecord) {			
			serverService.reportStolenAsset(device.getAddress());
		};
	};
	
	private long SCAN_DURATION = 2500;
	
	private Handler taskScheduler = new Handler();
	
	public void scan(/*, List<String> searchedUuid*/) {
		initiateBluetoothAdapter();
		startScanner();
		// return foundDevices;
	}

	private void log(String content) {
		Log.d(LOG_TAG, content);
	}
	
	void initiateBluetoothAdapter() {
		BluetoothManager bluetoothManager =
		        (BluetoothManager) context.getSystemService(Context.BLUETOOTH_SERVICE);
		bluetoothAdapter = bluetoothManager.getAdapter();
	}
	
    void startScanner() {
    	log("Starting bluetooth scanner for: " + SCAN_DURATION + " [milliseconds] ...");
        bluetoothAdapter.startLeScan(serverService.getStoleAssets(), bluetoothCallback);
        taskScheduler.postDelayed(scannerStopCommand, SCAN_DURATION);
    }
    
    Runnable scannerStopCommand = new Runnable() {
        @Override
        public void run() {
            stopScanner();
        }
    };
	
    void stopScanner() {
    	log("Stopping bluetooth scanner.");
        bluetoothAdapter.stopLeScan(bluetoothCallback);
    }
}
