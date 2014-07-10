package eu.appbucket.beaconmonitor.core;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import android.util.Log;

public class ServerService {
	
	private static final String LOG_TAG = ServerService.class.getName();
	
	public UUID[] getStoleAssets() {
		List<UUID> stoleAssets = new ArrayList<UUID>();
		stoleAssets.add(UUID.fromString("f4c36eac-0767-11e4-a4ed-b2227cce2b54"));
		UUID[] stolenUUIDs = new UUID[stoleAssets.size()];
		stoleAssets.toArray(stolenUUIDs);
		return stolenUUIDs;
	}
	
	public void reportStolenAsset(String foundAsset) {
		Log.d(LOG_TAG, "Reporting found assets: " + foundAsset);
	}
}
