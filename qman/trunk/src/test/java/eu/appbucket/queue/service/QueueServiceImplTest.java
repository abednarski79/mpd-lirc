package eu.appbucket.queue.service;

import static org.junit.Assert.assertEquals;

import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

import org.junit.Before;
import org.junit.Test;

import eu.appbucket.queue.core.domain.queue.OpeningHours;
import eu.appbucket.queue.core.domain.queue.OpeningTimes;
import eu.appbucket.queue.core.service.QueueServiceImpl;

public class QueueServiceImplTest {
	
	private QueueServiceImpl sut;
	
	@Before
	public void setup() {
		sut = new QueueServiceImpl() {			
			@Override
			protected Date getNewDate() {			
				return new Date(0);
			}
		};
	}
	
	@Test
	public void testCalculateOpeningTime() {
		OpeningHours openingHours = new OpeningHours();
		openingHours.setOpeningHour(9);
		openingHours.setOpeningMinute(30);
		openingHours.setClosingHour(17);
		openingHours.setClosingMinute(30);
		OpeningTimes actualOpeningTimes = sut.calculateOpeningTime(openingHours);
		Calendar calendar = Calendar.getInstance();
		calendar.setTimeInMillis(0);
		calendar.set(Calendar.HOUR_OF_DAY, openingHours.getOpeningHour());
		calendar.set(Calendar.MINUTE, openingHours.getOpeningMinute());
		long expectedOpeningTime = calendar.getTime().getTime();
		calendar.setTimeInMillis(0);
		calendar.set(Calendar.HOUR_OF_DAY, openingHours.getClosingHour());
		calendar.set(Calendar.MINUTE, openingHours.getClosingMinute());
		long expectedClosingTime = calendar.getTime().getTime();
		assertEquals(expectedOpeningTime, actualOpeningTimes.getOpeningTime());
		assertEquals(expectedClosingTime, actualOpeningTimes.getClosingTime());
	}
}
