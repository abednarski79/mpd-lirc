package eu.appbucket.queue.core.service.estimator.duration;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

import eu.appbucket.queue.core.domain.queue.OpeningTimes;
import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;

public class DefaultWaitingTimeEsimationStrategyImplTest {
	
	private DefaultWaitingTimeEsimationStrategyImpl sut;
	
	@Before
	public void setup() {
		sut = new DefaultWaitingTimeEsimationStrategyImpl();
	}
	
	@Test
	public void test(){
		final long openingTimeTimestamp = 25;
		final int averageWaitingTime = 50;
		int ticketNumber = 100;
		final OpeningTimes todayOpeningTimesUTC = new OpeningTimes();
		todayOpeningTimesUTC.setOpeningTime(openingTimeTimestamp);
		QueueDetails queueDetails = new QueueDetails() {
			public OpeningTimes getTodayOpeningTimesUTC() {
				return todayOpeningTimesUTC;
			}
		};
		queueDetails.setDefaultAverageWaitingDuration(averageWaitingTime);
		TicketEstimation ticketStatus = sut.estimateTimeToBeServiced(queueDetails, null, ticketNumber);
		long actualServiceTime = ticketStatus.getTimeToBeServiced();
		long expectedServiceTime = (averageWaitingTime * (ticketNumber -1)) + openingTimeTimestamp;
		assertEquals(expectedServiceTime, actualServiceTime);
	}
}
