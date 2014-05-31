package eu.appbucket.queue.core.service.estimator.quality;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Calendar;
import java.util.Date;

import org.junit.Before;
import org.junit.Test;

import eu.appbucket.queue.core.domain.queue.OpeningTimes;
import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

public class TimeBasedInputQualityEstimatorImplTest {
	
	private TimeBasedInputQualityEstimatorImpl sut;
	private static final long OPENING_TIME = 0;
	private static final long CLOSING_TIME = 200;
	private static final long AVERAGE_SERVICE_DUATION = 10;
	
	@Before
	public void setup() {
		sut = new TimeBasedInputQualityEstimatorImpl();
	}
	
	private int estimateQualityWrapper(int servicedNumber, long entryTime) {
		return sut.estimateQuality(
				servicedNumber, AVERAGE_SERVICE_DUATION, entryTime,
				OPENING_TIME, CLOSING_TIME);
	}
	
	@Test
	public void testWhenEntryValueAndTimeAtLowBandForTopScore() {
		int servicedNumber = 10;
		long entryTimeAtLowBandForTopScore = 
				(servicedNumber - 1) * AVERAGE_SERVICE_DUATION + 1;		
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeAtLowBandForTopScore);
		assertEquals(TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueAndTimeAtHighBandForTopScore() {
		int servicedNumber = 10;
		long entryTimeAtLowBandForTopScore = 
				servicedNumber * AVERAGE_SERVICE_DUATION;		
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeAtLowBandForTopScore);
		assertEquals(TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE, actualEstimation);
	}
	
	@Test
	public void testWhenEntryTimeBeforeOpeningHour() {
		int servicedNumber = 1;
		long entryTimeBeforeOpeningHour = OPENING_TIME - 1;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeBeforeOpeningHour);;
		assertEquals(TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE, actualEstimation);
	}

	@Test
	public void testWhenEntryTimeAfterOpeningHour() {
		int servicedNumber = 1;
		long entryTimeBeforeOpeningHour = CLOSING_TIME + 1;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeBeforeOpeningHour);;
		assertEquals(TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueIsLowerThenExpectedValue() {
		int servicedNumber = 8;
		long entryTime = (servicedNumber + 4) * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);;
		assertTrue(actualEstimation > TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE);
		assertTrue(actualEstimation < TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE);
		assertEquals(36, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueIsHigherThenExpectedValue() {
		int servicedNumber = 10;
		long entryTime = (servicedNumber - 2) * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);
		assertTrue(actualEstimation > TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE);
		assertTrue(actualEstimation < TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE);
		assertEquals(84, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueIsOutOfTheAcceptedRange() {
		int servicedNumber = 20;
		long entryTime = (servicedNumber + 26) * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);
		assertEquals(TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE, actualEstimation);
	}
	
	@Test
	public void testEstimateInputQualityForTopScore() {
		QueueDetails queueDetails = build9To5OfficeQueueDetails();
		QueueStats queueStats = buildDefaultQueueStats();
		TicketUpdate ticketUpdate = new TicketUpdate();
		ticketUpdate.setCurrentlyServicedTicketNumber(5);
		ticketUpdate.setCreated(
				buildDateForServiceNumer(
					ticketUpdate.getCurrentlyServicedTicketNumber(),
					queueDetails.getDefaultAverageWaitingDuration(),
					queueDetails.getTodayOpeningTimesUTC().getOpeningTime()));
		int actualQuality = sut.estimateInputQuality(queueDetails, queueStats, ticketUpdate);
		assertEquals(TimeBasedInputQualityEstimator.MAX_QUALITY_SCORE, actualQuality);
	}
	
	private QueueStats buildDefaultQueueStats() {
		QueueStats queueStats = new QueueStats();
		queueStats.setCalculatedAverageWaitingDuration(null);
		return queueStats;
	}
	
	private QueueDetails build9To5OfficeQueueDetails() {
		final OpeningTimes openingTimesUTC = new OpeningTimes();
		openingTimesUTC.setOpeningTime(generateTimestampAt9AMInJanuary2010());
		openingTimesUTC.setClosingTime(generateTimestampAt5PMInJanuary2010());
		QueueDetails queueDetails = new QueueDetails() {
			public OpeningTimes getTodayOpeningTimesUTC() {
				return openingTimesUTC;
			}
		};
		queueDetails.setDefaultAverageWaitingDuration(144000); // about 2.4 min. / person
		return queueDetails;
	}
	
	private long generateTimestampAt9AMInJanuary2010() {
		Calendar calendar = generateCalenarAt1stOfJanuary2010();
		calendar.set(Calendar.HOUR_OF_DAY, 9);
		return calendar.getTimeInMillis();
	}
	
	private Calendar generateCalenarAt1stOfJanuary2010() {
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2010);
		calendar.set(Calendar.MONTH, 0);
		calendar.set(Calendar.DAY_OF_MONTH, 1);
		calendar.set(Calendar.HOUR_OF_DAY, 0);
		calendar.set(Calendar.MINUTE, 0);
		calendar.set(Calendar.SECOND, 0);
		calendar.set(Calendar.MILLISECOND, 0);
		return calendar;
	}
	
	private long generateTimestampAt5PMInJanuary2010() {
		Calendar calendar = generateCalenarAt1stOfJanuary2010();
		calendar.set(Calendar.HOUR_OF_DAY, 17);
		return calendar.getTimeInMillis();
	}
	
	private static Date buildDateForServiceNumer(int servicedNumber, int averageServiceDuarion, long officeOpeningTime) {
		long serviceTime = ((servicedNumber - 1) * averageServiceDuarion) + officeOpeningTime + (averageServiceDuarion / 2);
		Date dateForServiceNumer = new Date(serviceTime);
		return dateForServiceNumer;
	}
	
	private static Date buildStartDateForServiceNumer(int servicedNumber, int averageServiceDuarion, long officeOpeningTime) {
		long serviceTime = ((servicedNumber - 1) * averageServiceDuarion) + officeOpeningTime;
		Date dateForServiceNumer = new Date(serviceTime);
		return dateForServiceNumer;
	}
	
	private static Date buildEndDateForServiceNumer(int servicedNumber, int averageServiceDuarion, long officeOpeningTime) {
		long serviceTime = ((servicedNumber) * averageServiceDuarion) + officeOpeningTime;
		Date dateForServiceNumer = new Date(serviceTime);
		return dateForServiceNumer;
	}
	
	@Test
	public void testEstimateInputQualityForToEarlyEntry() {
		QueueDetails queueDetails = build9To5OfficeQueueDetails();
		QueueStats queueStats = buildDefaultQueueStats();
		TicketUpdate ticketUpdate = new TicketUpdate();
		ticketUpdate.setCurrentlyServicedTicketNumber(15);
		ticketUpdate.setCreated(
				buildDateForServiceNumer(
					(ticketUpdate.getCurrentlyServicedTicketNumber() - 1),
					queueDetails.getDefaultAverageWaitingDuration(),
					queueDetails.getTodayOpeningTimesUTC().getOpeningTime()));
		int actualQuality = sut.estimateInputQuality(queueDetails, queueStats, ticketUpdate);
		assertTrue(actualQuality < TimeBasedInputQualityEstimator.MAX_QUALITY_SCORE);
	}
	
	@Test
	public void testEstimateInputQualityForToLateEntry() {
		QueueDetails queueDetails = build9To5OfficeQueueDetails();
		QueueStats queueStats = buildDefaultQueueStats();
		TicketUpdate ticketUpdate = new TicketUpdate();
		ticketUpdate.setCurrentlyServicedTicketNumber(15);
		ticketUpdate.setCreated(
				buildDateForServiceNumer(
					(ticketUpdate.getCurrentlyServicedTicketNumber() + 2),
					queueDetails.getDefaultAverageWaitingDuration(),
					queueDetails.getTodayOpeningTimesUTC().getOpeningTime()));
		int actualQuality = sut.estimateInputQuality(queueDetails, queueStats, ticketUpdate);
		assertTrue(actualQuality < TimeBasedInputQualityEstimator.MAX_QUALITY_SCORE);
	}
	
	@Test
	public void testEstimateInputQualityForOutOfRange() {
		QueueDetails queueDetails = build9To5OfficeQueueDetails();
		QueueStats queueStats = buildDefaultQueueStats();
		TicketUpdate ticketUpdate = new TicketUpdate();
		ticketUpdate.setCurrentlyServicedTicketNumber(5);
		ticketUpdate.setCreated(
				buildDateForServiceNumer(
					(ticketUpdate.getCurrentlyServicedTicketNumber() - 5),
					queueDetails.getDefaultAverageWaitingDuration(),
					queueDetails.getTodayOpeningTimesUTC().getOpeningTime()));
		int actualQuality = sut.estimateInputQuality(queueDetails, queueStats, ticketUpdate);
		assertEquals(TimeBasedInputQualityEstimator.MIN_QUALITY_SCORE, actualQuality);
	}
		
	public static void main(String[] args) {
		int averageServiceDuration = 144000;
		int officeOpeningHour = 9;
		int officeOpeningMinute = 30;
		long officeOpeningTime = generateTimestampForTodayAndGivenTime(officeOpeningHour, officeOpeningMinute);
		System.out.println("Generating expected service time for the office with opening time: " + new Date(officeOpeningTime));
		for(int servicedNumber = 1; servicedNumber <= 200; servicedNumber ++) {
			Date predictedServiceTimeStart = buildStartDateForServiceNumer(servicedNumber, averageServiceDuration, officeOpeningTime);
			Date predictedServiceTimeEnd = buildEndDateForServiceNumer(servicedNumber, averageServiceDuration, officeOpeningTime);
			System.out.println(servicedNumber + " (" + predictedServiceTimeStart + ", " + predictedServiceTimeEnd + ">");
		}
	}
	
	private static long generateTimestampForTodayAndGivenTime(int hour, int minute) {
		Calendar calendar = Calendar.getInstance();
		calendar.setTime(new Date());
		calendar.set(Calendar.HOUR_OF_DAY, hour);
		calendar.set(Calendar.MINUTE, minute);
		calendar.set(Calendar.SECOND, 0);
		calendar.set(Calendar.MILLISECOND, 0);
		return calendar.getTimeInMillis();
	}
}
 