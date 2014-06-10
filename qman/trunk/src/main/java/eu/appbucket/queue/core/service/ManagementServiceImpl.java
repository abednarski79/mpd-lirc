package eu.appbucket.queue.core.service;

import org.springframework.cache.annotation.CacheEvict;
import org.springframework.stereotype.Service;

@Service
public class ManagementServiceImpl implements ManagementService {

	@CacheEvict(value = {"queuesCache", 
			"queueInfoCache", 
			"queueDetailsCache",
			"queueStatsCache",
			"highestTicketUpdateCache"}, allEntries = true)
	public void resetCaches() {
	}
}
