package eu.appbucket.beaconmonitor.core.service;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import android.util.Log;

public class CommunicationService {
	
	private static final String LOG_TAG = CommunicationService.class.getName();
	
	public UUID[] getStoleAssets() {
		List<UUID> stoleAssets = new ArrayList<UUID>();
		stoleAssets.add(UUID.fromString("F4C36EAC-0767-11E4-A4ED-B2227CCE2B54"));
		UUID[] stolenUUIDs = new UUID[stoleAssets.size()];
		stoleAssets.toArray(stolenUUIDs);
		return stolenUUIDs;
	}
	
	public void reportStolenAsset(String foundAsset) {
		Log.d(LOG_TAG, "Reporting found assets: " + foundAsset);
	}
}
