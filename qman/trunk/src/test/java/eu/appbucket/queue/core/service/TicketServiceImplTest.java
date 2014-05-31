package eu.appbucket.queue.core.service;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Collection;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import org.jmock.Expectations;
import org.jmock.Mockery;
import org.jmock.integration.junit4.JUnit4Mockery;
import org.junit.Before;
import org.junit.Test;

import eu.appbucket.queue.core.domain.queue.OpeningTimes;
import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public class TicketServiceImplTest {
	
	TicketServiceImpl sut;
	QueueService queueServiceMock;
	Mockery context = new JUnit4Mockery();
	
	@Before
	public void setup() {
		sut = new TicketServiceImpl();	
		queueServiceMock = context.mock(QueueService.class);
		sut.setQueueService(queueServiceMock);
	}
	
	@Test
	public void testGroupUpdatesForPerTicket() {
		Collection<TicketUpdate> ticketUpdates = new HashSet<TicketUpdate>();
		ticketUpdates.add(buildTicketUpdateForTicketNumber(1));
		ticketUpdates.add(buildTicketUpdateForTicketNumber(2));
		ticketUpdates.add(buildTicketUpdateForTicketNumber(2));
		ticketUpdates.add(buildTicketUpdateForTicketNumber(3));
		ticketUpdates.add(buildTicketUpdateForTicketNumber(3));
		ticketUpdates.add(buildTicketUpdateForTicketNumber(3));
		Map<Integer, Set<TicketUpdate>> actualGroups = sut.groupUpdatesForPerTicket(ticketUpdates);		
		assertEquals(1, actualGroups.get(1).size());
		assertEquals(2, actualGroups.get(2).size());
		assertEquals(3, actualGroups.get(3).size());
		assertEquals(1, actualGroups.get(1).iterator().next().getCurrentlyServicedTicketNumber());
		assertEquals(2, actualGroups.get(2).iterator().next().getCurrentlyServicedTicketNumber());
		assertEquals(3, actualGroups.get(3).iterator().next().getCurrentlyServicedTicketNumber());
	}
	
	private TicketUpdate buildTicketUpdateForTicketNumber(int ticketNumber) {
		TicketUpdate ticketUpdate = new TicketUpdate();
		ticketUpdate.setCurrentlyServicedTicketNumber(ticketNumber);
		ticketUpdate.setCreated(new Date());
		return ticketUpdate;
	}
	
	@Test
	public void testCalculateAverageServiceDurations() {
		Map<Integer, Set<TicketUpdate>> ticketNumberToUpdates = new HashMap<Integer, Set<TicketUpdate>>();
		Set<TicketUpdate> ticketUpdates1 = new HashSet<TicketUpdate>();
		ticketUpdates1.add(buildTicketUpdateForTicketNumberAndDate(1, 3));
		ticketUpdates1.add(buildTicketUpdateForTicketNumberAndDate(1, 6));
		ticketUpdates1.add(buildTicketUpdateForTicketNumberAndDate(1, 9));
		ticketNumberToUpdates.put(1, ticketUpdates1);
		Set<TicketUpdate> ticketUpdates2 = new HashSet<TicketUpdate>();
		ticketUpdates2.add(buildTicketUpdateForTicketNumberAndDate(2, 20));
		ticketUpdates2.add(buildTicketUpdateForTicketNumberAndDate(2, 30));
		ticketUpdates2.add(buildTicketUpdateForTicketNumberAndDate(2, 40));
		ticketNumberToUpdates.put(2, ticketUpdates2);
		final QueueInfo queueInfo = new QueueInfo();
		queueInfo.setQueueId(1);
		final OpeningTimes openingTimes = new OpeningTimes();
		openingTimes.setOpeningTime(0);
		final QueueDetails queueDetails = new QueueDetails() {
			public OpeningTimes getTodayOpeningTimesUTC() {
				return openingTimes;
			}
		};
		context.checking(new Expectations() {{
            oneOf(queueServiceMock).getQueueDetailsByQueueId(queueInfo.getQueueId());
            will(returnValue(queueDetails));
		}});
		Set<Integer> actualAverageServiceDurations = 
				sut.calculateAverageServiceDurations(ticketNumberToUpdates, queueInfo);
		assertEquals(2, actualAverageServiceDurations.size());
		assertTrue(actualAverageServiceDurations.contains(6));
		assertTrue(actualAverageServiceDurations.contains(15));
	}
	
	private TicketUpdate buildTicketUpdateForTicketNumberAndDate(int ticketNumber, long timeStamp) {
		TicketUpdate ticketUpdate = buildTicketUpdateForTicketNumber(ticketNumber);
		ticketUpdate.setCreated(new Date(timeStamp));
		return ticketUpdate;
	}
	
	@Test
	public void testCalculateOverallAverageServiceDuration(){
		Set<Integer> averageServiceDurations = new HashSet<Integer>();
		averageServiceDurations.add(20);
		averageServiceDurations.add(40);
		averageServiceDurations.add(80);
		averageServiceDurations.add(100);
		int actualOverallAverageServiceDuration = 
				sut.calculateOverallAverageServiceDuration(averageServiceDurations);
		assertEquals(60, actualOverallAverageServiceDuration);
	}
}
