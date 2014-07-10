package eu.appbucket.beaconmonitor.core;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

public class BootReceiver extends BroadcastReceiver {

	private static final String BOOT_COMPLETE_ACTION = "android.intent.action.BOOT_COMPLETED";
	
	@Override
    public void onReceive(Context context, Intent intent) {
        if (intent.getAction().equals(BOOT_COMPLETE_ACTION)) {
            // Set the alarm here.
        }
    }
	
	
}
