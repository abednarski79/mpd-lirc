package eu.appbucket.queue.core.service;

import org.springframework.stereotype.Service;

import com.googlecode.ehcache.annotations.TriggersRemove;
import com.googlecode.ehcache.annotations.When;

@Service
public class ManagementServiceImpl implements ManagementService {

	@TriggersRemove(cacheName = {"queuesCache", 
			"queueInfoCache", 
			"queueDetailsCache",
			"queueStatsCache",
			"highestTicketUpdateCache"}, 
		when = When.AFTER_METHOD_INVOCATION, removeAll = true)
	public void resetCaches() {
	}
}
