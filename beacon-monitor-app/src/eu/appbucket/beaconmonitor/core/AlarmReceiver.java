package eu.appbucket.beaconmonitor.core;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

public class AlarmReceiver extends BroadcastReceiver {

	@Override
	public void onReceive(Context context, Intent intent) {
		ScannerService scanner = new ScannerService(context);
		scanner.scan();
	}
}
