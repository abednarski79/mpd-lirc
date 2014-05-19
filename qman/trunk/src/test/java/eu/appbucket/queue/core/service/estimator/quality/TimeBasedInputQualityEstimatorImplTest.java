package eu.appbucket.queue.core.service.estimator.quality;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import eu.appbucket.queue.core.service.estimator.quality.TimeBasedInputQualityEstimatorImpl;

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
	public void testWhenEntryValueLowerThenExpectedValue() {
		int servicedNumber = 8;
		long entryTime = 2 * servicedNumber * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);;
		assertTrue(actualEstimation > TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE);
		assertTrue(actualEstimation < TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE);
		assertEquals(84, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueHigherThenExpectedValue() {
		int servicedNumber = 10;
		long entryTime = (servicedNumber / 2 ) * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);
		assertTrue(actualEstimation > TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE);
		assertTrue(actualEstimation < TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE);
		assertEquals(94, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueOutOfTheAcceptedRange() {
		int servicedNumber = 20;
		long entryTime = (servicedNumber + 26) * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);
		assertEquals(TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE, actualEstimation);
	}
}
