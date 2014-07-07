package eu.appbucket.beaconmonitor.ui;

import java.util.Date;

import eu.appbucket.beaconmonitor.R;
import eu.appbucket.beaconmonitor.service.MonitorService;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothAdapter.LeScanCallback;
import android.bluetooth.BluetoothManager;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class UserInterfaceActivity extends Activity {

	private static final String LOG_TAG = 
			UserInterfaceActivity.class.getName() 
			+ UserInterfaceActivity.class.getPackage().getName();
	
	boolean isServiceRunning = false;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		Button scanBtn = (Button) findViewById(R.id.btnScan);
		scanBtn.setOnClickListener(new View.OnClickListener() {
			Button scanBtn = (Button) findViewById(R.id.btnScan);
			@Override
			public void onClick(View v) {
				if(isServiceRunning) {
					stopService();
					isServiceRunning = false;
					scanBtn.setText("Start scanning");
				} else {
					isServiceRunning = true;
					startService();
					scanBtn.setText("Stop scanning");	
				}
			}
		});
	}
	
	public void startService(/*View view*/) {
		startService(new Intent(getBaseContext(), MonitorService.class));
	}
	
	public void stopService(/*View view*/) {
		stopService(new Intent(getBaseContext(), MonitorService.class));
	}
	
	/*public void appendLog(String logLine) {
		Log.d(LOG_TAG, logLine);
		TextView logArea = (TextView) findViewById(R.id.TEXT_STATUS_ID);
		logArea.setText(new Date().toString() + " - " + logLine + "\n" + logArea.getText());
	}*/
}
