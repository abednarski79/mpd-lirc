package eu.appbucket.queue.core.service.estimator.quality;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public class TimeBasedInputQualityEstimatorImpl implements TimeBasedInputQualityEstimator {

	public int estimateQuality(QueueDetails queueDetails,
			QueueStats queueStats, TicketUpdate ticketUpdate) {
		int averageWaitingDuarion = 
				queueStats.getCalculatedAverageWaitingDuration() != null ? 
						queueStats.getCalculatedAverageWaitingDuration() : queueDetails.getDefaultAverageWaitingDuration();
		int servicedNumber = ticketUpdate.getCurrentlyServicedTicketNumber();
		int entryTime = 0; // TODO: ticketUpdate.getCreated().getTime();
				
		return 0; //TODO: call estimateQuality
	}
	
	protected int estimateQuality(
			int servicedNumber, int averageWaitingDuarion, int entryTime,
			int minAccepterEntryTime, int maxAccepterEntryTime) {
		if(entryTime < minAccepterEntryTime) {
			return MIN_QUALITY_SCORE;
		}
		if(entryTime > maxAccepterEntryTime) {
			return MIN_QUALITY_SCORE;
		}
		int minTopScoreEntryTime = (servicedNumber - 1) * averageWaitingDuarion;
		int maxTopScoreEntryTime = servicedNumber * averageWaitingDuarion;
		if(entryTime > minTopScoreEntryTime && entryTime <= maxTopScoreEntryTime) {
			return MAX_QUALITY_SCORE;
		}
		return estimateQualityBasedOnParabolaEquasion(servicedNumber, averageWaitingDuarion, entryTime);
	}
	
	private int estimateQualityBasedOnParabolaEquasion(int servicedNumber, int averageServiceDuarion, int entryTime) {
		double parabolaEquastionDirectionalParameter = (double) MAX_QUALITY_SCORE / ((double) MAX_ACCEPTED_SERVICE_NUMBER_RANGE * ((-1) * (double) MAX_ACCEPTED_SERVICE_NUMBER_RANGE));		
		double highestScoreServiceNumber = entryTime / averageServiceDuarion;
		double normalizedServicedNumer = servicedNumber - highestScoreServiceNumber;
		double estimation = 
				parabolaEquastionDirectionalParameter 
				* (normalizedServicedNumer - (double) MAX_ACCEPTED_SERVICE_NUMBER_RANGE)
				* (normalizedServicedNumer + (double) MAX_ACCEPTED_SERVICE_NUMBER_RANGE);
		if(estimation < 0) {
			estimation = MIN_QUALITY_SCORE;
		}
		return (int) Math.ceil(estimation);
	}
}
