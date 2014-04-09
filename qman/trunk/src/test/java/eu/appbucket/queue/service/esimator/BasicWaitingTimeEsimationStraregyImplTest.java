package eu.appbucket.queue.service.esimator;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

import eu.appbucket.queue.domain.queue.OpeningTimes;
import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.domain.ticket.TicketStats;
import eu.appbucket.queue.service.estimator.BasicWaitingTimeEsimationStraregyImpl;

public class BasicWaitingTimeEsimationStraregyImplTest {
	
	BasicWaitingTimeEsimationStraregyImpl sut = null;
	
	@Before
	public void setup() {
		sut = new BasicWaitingTimeEsimationStraregyImpl();
	}
	
	@Test
	public void test(){
		QueueDetails queueDetails = new QueueDetails();
		long openingTimeTimestamp = 25;
		long averageWaitingTime = 50;
		int ticketNumber = 100;
		OpeningTimes openingTimes = new OpeningTimes();
		openingTimes.setOpeningTime(openingTimeTimestamp);
		queueDetails.setOpeningTimes(openingTimes);
		QueueStats queueStats = new QueueStats();
		queueStats.setAverageWaitingTime(averageWaitingTime);
		TicketStats ticketStatus = sut.estimateWaitingTime(queueDetails, queueStats, ticketNumber);
		long actualServiceTime = ticketStatus.getServiceTime();
		long expectedServiceTime = (averageWaitingTime * (ticketNumber -1)) + openingTimeTimestamp;
		assertEquals(expectedServiceTime, actualServiceTime);
	}
}