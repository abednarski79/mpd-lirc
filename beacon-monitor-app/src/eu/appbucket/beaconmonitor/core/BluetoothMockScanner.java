package eu.appbucket.beaconmonitor.core;

import android.content.Context;
import android.widget.Toast;

public class BluetoothMockScanner {
	
	private Context context;
	
	public BluetoothMockScanner(Context context) {
		this.context = context;
	}
	
	public void scan() {
		Toast toast = Toast.makeText(context, "Alarm just kicked off", Toast.LENGTH_SHORT);
		toast.show();	
	}
	
}
