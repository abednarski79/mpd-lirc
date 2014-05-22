package eu.appbucket.queue.core.service.estimator.quality;

import org.springframework.stereotype.Component;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

@Component
public class TimeBasedInputQualityEstimatorImpl implements TimeBasedInputQualityEstimator {

	public int estimateInputQuality(QueueDetails queueDetails,
			QueueStats queueStats, TicketUpdate ticketUpdate) {
		int averageWaitingDuration = findBestAvailableAverageWaitingDuration(queueDetails, queueStats);
		int servicedNumber = ticketUpdate.getCurrentlyServicedTicketNumber();
		long entryTime = ticketUpdate.getCreated().getTime();
		long openingTime = queueDetails.getOpeningTimesUTC().getOpeningTime();
		long closingTime = queueDetails.getOpeningTimesUTC().getClosingTime();
		return estimateQuality(servicedNumber, averageWaitingDuration, entryTime, 
				openingTime, closingTime);
	}
	
	private int findBestAvailableAverageWaitingDuration(QueueDetails queueDetails, QueueStats queueStats) {
		if(queueStats.getCalculatedAverageWaitingDuration() != null) {
			return queueStats.getCalculatedAverageWaitingDuration();
		}
		return queueDetails.getDefaultAverageWaitingDuration();
	}
	
	protected int estimateQuality(
			int servicedNumber, long averageWaitingDuration, long entryTime,
			long minAccepterEntryTime, long maxAccepterEntryTime) {
		if(entryTime < minAccepterEntryTime) {
			return MIN_QUALITY_SCORE;
		}
		if(entryTime > maxAccepterEntryTime) {
			return MIN_QUALITY_SCORE;
		}
		// TODO: ta kalkulacja jest bledna, powinna zaczyna od entryTime a nie od podanego numeru
		// na tej podstawie powinna obliczac aktualny 100% number i spr czy rowny jest z podanym
		long minTopScoreEntryTime = ((servicedNumber - 1) * averageWaitingDuration) + minAccepterEntryTime;
		long maxTopScoreEntryTime = (servicedNumber * averageWaitingDuration) + minAccepterEntryTime;
		if(entryTime > minTopScoreEntryTime && entryTime <= maxTopScoreEntryTime) {
			return MAX_QUALITY_SCORE;
		}
		long normalizedEntryTime = entryTime - minAccepterEntryTime;
		return estimateQualityBasedOnParabolaEquasion(servicedNumber, averageWaitingDuration, normalizedEntryTime);
	}
	
	private int estimateQualityBasedOnParabolaEquasion(long servicedNumber, long averageServiceDuration, long entryTime) {
		double parabolaEquastionDirectionalParameter = 
				(double) MAX_QUALITY_SCORE / 
				((double) MAX_ACCEPTED_SERVICE_NUMBER_RANGE * ((-1) * (double) MAX_ACCEPTED_SERVICE_NUMBER_RANGE));		
		double highestScoreServiceNumber = entryTime / averageServiceDuration;
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
