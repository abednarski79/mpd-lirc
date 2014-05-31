package eu.appbucket.queue.core.domain.queue;

import static org.junit.Assert.assertEquals;

import java.util.Calendar;

import org.junit.Before;
import org.junit.Test;

public class QueueDetailsTest {
	
	QueueDetails sut;
	
	@Before
	public void setup() {
		sut = new QueueDetails();
	}
	
	@Test
	public void testCalculateOpeningTime() {
		OpeningHours openingHours = new OpeningHours();
		openingHours.setOpeningHour(9);
		openingHours.setOpeningMinute(30);
		openingHours.setClosingHour(17);
		openingHours.setClosingMinute(30);
		OpeningTimes actualOpeningTimes = sut.calculateOpeningTimeUTC(openingHours);
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.HOUR_OF_DAY, openingHours.getOpeningHour());
		calendar.set(Calendar.MINUTE, openingHours.getOpeningMinute());
		calendar.set(Calendar.SECOND, 0);
		calendar.set(Calendar.MILLISECOND, 0);
		long expectedOpeningTime = calendar.getTimeInMillis();
		calendar.set(Calendar.HOUR_OF_DAY, openingHours.getClosingHour());
		calendar.set(Calendar.MINUTE, openingHours.getClosingMinute());
		calendar.set(Calendar.SECOND, 0);
		calendar.set(Calendar.MILLISECOND, 0);
		long expectedClosingTime = calendar.getTimeInMillis();
		assertEquals(expectedOpeningTime, actualOpeningTimes.getOpeningTime());
		assertEquals(expectedClosingTime, actualOpeningTimes.getClosingTime());
	}
}
