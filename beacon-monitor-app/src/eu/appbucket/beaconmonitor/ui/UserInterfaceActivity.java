package eu.appbucket.beaconmonitor.ui;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import eu.appbucket.beaconmonitor.R;
import eu.appbucket.beaconmonitor.core.ServiceScheduler;

public class UserInterfaceActivity extends Activity {

	private static final String LOG_TAG = UserInterfaceActivity.class.getName();
	private ServiceScheduler serviceScheduler;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		serviceScheduler = new ServiceScheduler(this.getApplicationContext());
		Button switchBtn = (Button) findViewById(R.id.btnSwitch);
		switchBtn.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
					if(serviceScheduler.isSchedulerActive()) {
						stopService();
					} else {
						startService();
					}
				}
			}
		);
		Button startBtn = (Button) findViewById(R.id.btnStart);
		startBtn.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
					startService();
					Log.d(LOG_TAG, "Scheduler is running: " + serviceScheduler.isSchedulerActive());
				}
			}
		);
		Button stopBtn = (Button) findViewById(R.id.btnStop);
		stopBtn.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
					stopService();
					Log.d(LOG_TAG, "Scheduler is running: " + serviceScheduler.isSchedulerActive());
				}
			}
		);
		Button checkBtn = (Button) findViewById(R.id.btnCheck);
		checkBtn.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
					Log.d(LOG_TAG, "Scheduler is running: " + serviceScheduler.isSchedulerActive());
				}
			}
		);
	}
	
	/*@Override
	protected void onResume() {
		super.onResume();
		//setButtonLabel();
	}*/
	
	/*private void setButtonLabel() {
		Button startBtn = (Button) findViewById(R.id.btnStart);
		if(serviceScheduler.isSchedulerActive()) {
			startBtn.setText("Stop scheduler.");
		} else {
			startBtn.setText("Start scheduler.");
		}
	}*/
	
	public void startService(/*View view*/) {
		serviceScheduler.startScheduler();
	}
	
	public void stopService(/*View view*/) {
		serviceScheduler.stopScheduler();
	}
}
