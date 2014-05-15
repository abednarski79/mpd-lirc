package eu.appbucket.queue.core.service.esimator;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

import eu.appbucket.queue.core.domain.queue.OpeningTimes;
import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;
import eu.appbucket.queue.core.service.estimator.CalculatedWaitingTimeEsimationStrategyImpl;

public class CalculatedWaitingTimeEsimationStrategyImplTest {
	
	CalculatedWaitingTimeEsimationStrategyImpl sut = null;
	
	@Before
	public void setup() {
		sut = new CalculatedWaitingTimeEsimationStrategyImpl();
	}
	
	@Test
	public void test(){
		QueueDetails queueDetails = new QueueDetails();
		long openingTimeTimestamp = 25;
		int averageWaitingTime = 50;
		int ticketNumber = 100;
		OpeningTimes openingTimes = new OpeningTimes();
		openingTimes.setOpeningTime(openingTimeTimestamp);
		queueDetails.setOpeningTimesUTC(openingTimes);
		QueueStats queueStats = new QueueStats();
		queueStats.setCalculatedAverageWaitingDuration(averageWaitingTime);
		TicketEstimation ticketStatus = sut.estimateTimeToBeServiced(queueDetails, queueStats, ticketNumber);
		long actualServiceTime = ticketStatus.getTimeToBeServiced();
		long expectedServiceTime = (averageWaitingTime * (ticketNumber -1)) + openingTimeTimestamp;
		assertEquals(expectedServiceTime, actualServiceTime);
	}
}
