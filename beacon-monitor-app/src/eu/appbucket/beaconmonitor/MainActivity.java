package eu.appbucket.beaconmonitor;

import java.util.Date;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothAdapter.LeScanCallback;
import android.bluetooth.BluetoothManager;
import android.content.Context;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends Activity {

	private static final String LOG_TAG = 
			MainActivity.class.getName() 
			+ MainActivity.class.getPackage().getName();
	
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
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		initiateBluetoothAdapter();
		
		Button scanBtn = (Button) findViewById(R.id.btnScan);
		scanBtn.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				startScanner();
			}
		});
	}
	
	public void initiateBluetoothAdapter() {
		BluetoothManager bluetoothManager =
		        (BluetoothManager) getSystemService(Context.BLUETOOTH_SERVICE);
		bluetoothAdapter = bluetoothManager.getAdapter();
	}
	public void appendLog(String logLine) {
		Log.d(LOG_TAG, logLine);
		TextView logArea = (TextView) findViewById(R.id.TEXT_STATUS_ID);
		logArea.setText(new Date().toString() + " - " + logLine + "\n" + logArea.getText());
	}
	
	@Override
	protected void onPause() {
		super.onPause();
		removeCallbacks();
		stopScanner();
	}
	
	private void removeCallbacks() {
		messageHandler.removeCallbacks(scannerStopCommand);
	}
    
    private void startScanner() {
    	disableButton();
    	appendLog("Starting bluetooth scanner for: " + SCAN_DURATION + " [milliseconds] ...");
        bluetoothAdapter.startLeScan(bluetoothCallback);
        messageHandler.postDelayed(scannerStopCommand, SCAN_DURATION);
    }
	
    public void disableButton() {
    	Button scanBtn = (Button) findViewById(R.id.btnScan);
    	scanBtn.setEnabled(false);
    }
    
	private Runnable scannerStopCommand = new Runnable() {
        @Override
        public void run() {
            stopScanner();
        }
    };
    
    private void stopScanner() {
    	appendLog("Stopping bluetooth scanner.");
        bluetoothAdapter.stopLeScan(bluetoothCallback);
        enableButton();
    }
    
    public void enableButton() {
    	Button scanBtn = (Button) findViewById(R.id.btnScan);
    	scanBtn.setEnabled(true);
    }
}
