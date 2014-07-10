package eu.appbucket.beaconmonitor.core;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.SystemClock;
import android.util.Log;

public class ServiceScheduler {
	
	private static final String LOG_TAG = 
			ServiceScheduler.class.getName();
	
	private Context context;
	private static final long MINUTESx10 = 1000 * 60 * 10;
	private static final long SECONDSx10 = 1000 * 10;
	private static final long SECONDSx1 = 1000;
	private static final long ALARM_INTERVAL = SECONDSx10;
	
	public ServiceScheduler(Context context) {
		this.context = context;
		
	}
	
	public void startScheduler() {
		log("Starting the scheduler.");
		PendingIntent alarmIntent = cerateNewAlarmIntent();
		AlarmManager alarmManager = createNewAlarmManager();
		alarmManager.setInexactRepeating(AlarmManager.ELAPSED_REALTIME_WAKEUP , 0, ALARM_INTERVAL, alarmIntent);
	}
	
	public void stopScheduler() {
		log("Canceling the scheduler.");
		PendingIntent alarmIntent = cerateNewAlarmIntent();
		AlarmManager alarmManager = createNewAlarmManager();
		if(alarmManager != null) {
			alarmManager.cancel(alarmIntent);
			alarmIntent.cancel();
		}
	}
	
	public boolean isSchedulerActive() {
		PendingIntent alreadySchedulerAlarmIntent = retrieveExistingAlarmIntent();
		return alreadySchedulerAlarmIntent != null;
	}
	
	private AlarmManager createNewAlarmManager() {
		AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
		return alarmManager;
	}
	
	private PendingIntent cerateNewAlarmIntent() {
		Intent intent = new Intent(context, AlarmReceiver.class);
		PendingIntent alarmIntent = PendingIntent.getBroadcast(context, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
		return alarmIntent;
	}
	
	private PendingIntent retrieveExistingAlarmIntent() {
		Intent intent = new Intent(context, AlarmReceiver.class);
		PendingIntent alreadySchedulerAlarmIntent = 
				PendingIntent.getBroadcast(context, 0, intent, PendingIntent.FLAG_NO_CREATE);
		return alreadySchedulerAlarmIntent;
	}
	
	private void log(String content) {
		Log.d(LOG_TAG, content);
	}
}
