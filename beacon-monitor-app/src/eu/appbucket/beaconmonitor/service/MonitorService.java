package eu.appbucket.beaconmonitor.service;

import android.app.Service;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothAdapter.LeScanCallback;
import android.bluetooth.BluetoothManager;
import android.content.Context;
import android.content.Intent;
import android.os.Handler;
import android.os.IBinder;
import android.os.Message;
import android.util.Log;
import android.widget.Toast;

public class MonitorService extends Service {

	private static final String LOG_TAG = 
			MonitorService.class.getName() 
			+ MonitorService.class.getPackage().getName();
	
	private BluetoothAdapter bluetoothAdapter;
	
	private LeScanCallback bluetoothCallback = new LeScanCallback() {
		public void onLeScan(android.bluetooth.BluetoothDevice device, int rssi, byte[] scanRecord) {			
			messageHandler.sendMessage(Message.obtain(null, MSG_TYPE_DEVICE_FOUND, 
					device.getName() + " = " + device.getAddress()));
		};
	};
	private long SCAN_DURATION = 2500;
	
	private static final int MSG_TYPE_DEVICE_FOUND = 1;
	
	private Handler messageHandler = new Handler() {
		@Override
		public void handleMessage(Message message) {
			switch (message.what) {
				case MSG_TYPE_DEVICE_FOUND:
					appendLog("Device found." + (String) message.obj);
					break;
			}
		}
	};
	
	@Override
	public IBinder onBind(Intent intent) {
		return null;
	}

	@Override
	public int onStartCommand(Intent intent, int flags, int startId) {
		Log.d(LOG_TAG, "Starting service");
		initiateBluetoothAdapter();
		startScanner();
		return START_STICKY;
	}
	
	void initiateBluetoothAdapter() {
		BluetoothManager bluetoothManager =
		        (BluetoothManager) getSystemService(Context.BLUETOOTH_SERVICE);
		bluetoothAdapter = bluetoothManager.getAdapter();
	}
	
    void startScanner() {
    	appendLog("Starting bluetooth scanner for: " + SCAN_DURATION + " [milliseconds] ... [startScanner]");
        bluetoothAdapter.startLeScan(bluetoothCallback);
        messageHandler.postDelayed(scannerStopCommand, SCAN_DURATION);
    }
    
    Runnable scannerStopCommand = new Runnable() {
        @Override
        public void run() {
            stopScanner();
        }
    };
    
	@Override
	public void onDestroy() {
		super.onDestroy();
		removeCallbacks();
		stopScanner();
		Log.d(LOG_TAG, "Stoping service");
		appendLog("Stopping bluetooth scanner. [onDestroy]");
	}
	
	private void removeCallbacks() {
		messageHandler.removeCallbacks(scannerStopCommand);
	}
	
    void stopScanner() {
    	appendLog("Stopping bluetooth scanner. [stopScanner]");
        bluetoothAdapter.stopLeScan(bluetoothCallback);
    }
    
	void appendLog(String log) {
		Toast.makeText(this, log, Toast.LENGTH_SHORT).show();
	}
}
