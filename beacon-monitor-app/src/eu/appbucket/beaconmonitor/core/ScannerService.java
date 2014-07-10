package eu.appbucket.beaconmonitor.core;

import java.util.List;

import android.content.Context;
import android.util.Log;

public class ScannerService {
	
	private static final String LOG_TAG = 
			ScannerService.class.getName();
	
	private Context context;
	
	public ScannerService(Context context) {
		this.context = context;
	}
	
	public void scan() {
		log("Running scanner... ");
		BluetoothScanner scanner = new BluetoothScanner(context);
		// BluetoothMockScanner scanner = new BluetoothMockScanner(context);
		scanner.scan();
	}
	
	private void log(String content) {
		Log.d(LOG_TAG, content);
	}
}
