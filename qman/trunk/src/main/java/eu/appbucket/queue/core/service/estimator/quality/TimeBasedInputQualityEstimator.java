package eu.appbucket.queue.core.service.estimator.quality;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public interface TimeBasedInputQualityEstimator {
	
	final static int MAX_QUALITY_SCORE = 100;
	final static int MIN_QUALITY_SCORE = 0;
	final static int MAX_ACCEPTED_SERVICE_NUMBER_RANGE = 5;

	/**
	 * Estimates quality of inputed serviced number based on average service duration and entry time.
	 * 
	 * @param queueDetails details of the queue
	 * @param queueStats statistics of the queue
	 * @param ticketUpdate input data
	 * @return estimated quality of input, it ranges from 0 to 100 where 0 marks
	 * result which can not be accepted and 100 is fully accepted input.
	 */
	int estimateInputQuality(QueueDetails queueDetails, QueueStats queueStats, TicketUpdate ticketUpdate);
}
