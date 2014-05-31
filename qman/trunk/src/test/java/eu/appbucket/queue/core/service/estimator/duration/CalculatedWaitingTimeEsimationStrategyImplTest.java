package eu.appbucket.queue.core.service.estimator.duration;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

import eu.appbucket.queue.core.domain.queue.OpeningTimes;
import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;
import eu.appbucket.queue.core.service.estimator.duration.CalculatedWaitingTimeEsimationStrategyImpl;

public class CalculatedWaitingTimeEsimationStrategyImplTest {
	
	CalculatedWaitingTimeEsimationStrategyImpl sut = null;
	
	@Before
	public void setup() {
		sut = new CalculatedWaitingTimeEsimationStrategyImpl();
	}
	
	@Test
	public void test(){
		long openingTimeTimestamp = 25;
		int averageWaitingTime = 50;
		int ticketNumber = 100;
		final OpeningTimes todayOpeningTimesUTC = new OpeningTimes();
		todayOpeningTimesUTC.setOpeningTime(openingTimeTimestamp);
		QueueDetails queueDetails = new QueueDetails() {
			public OpeningTimes getTodayOpeningTimesUTC() {
				return todayOpeningTimesUTC;
			}
		};
		QueueStats queueStats = new QueueStats();
		queueStats.setCalculatedAverageWaitingDuration(averageWaitingTime);
		TicketEstimation ticketStatus = sut.estimateTimeToBeServiced(queueDetails, queueStats, ticketNumber);
		long actualServiceTime = ticketStatus.getTimeToBeServiced();
		long expectedServiceTime = (averageWaitingTime * (ticketNumber -1)) + openingTimeTimestamp;
		assertEquals(expectedServiceTime, actualServiceTime);
	}
}
