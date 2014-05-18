package eu.appbucket.queue.core.service.estimator.duration;

import eu.appbucket.queue.core.domain.queue.QueueStats;

public interface WaitingTimeEstimatorStrategyFactory {
	
	WaitingTimeEsimationStrategy getStrategy(QueueStats queueStats);
}
