package eu.appbucket.queue.core.service.esimator.quality;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import eu.appbucket.queue.core.service.estimator.quality.TimeBasedInputQualityEstimatorImpl;

public class TimeBasedInputQualityEstimatorImplTest {
	
	private TimeBasedInputQualityEstimatorImpl sut;
	private static final int OPENING_TIME = 0;
	private static final int CLOSING_TIME = 200;
	private static final int AVERAGE_SERVICE_DUATION = 10;
	
	@Before
	public void setup() {
		sut = new TimeBasedInputQualityEstimatorImpl();
	}
	
	private int estimateQualityWrapper(int servicedNumber, int entryTime) {
		return sut.estimateQuality(
				servicedNumber, AVERAGE_SERVICE_DUATION, entryTime,
				OPENING_TIME, CLOSING_TIME);
	}
	
	@Test
	public void testWhenEntryValueAndTimeAtLowBandForTopScore() {
		int servicedNumber = 10;
		int entryTimeAtLowBandForTopScore = 
				(servicedNumber - 1) * AVERAGE_SERVICE_DUATION + 1;		
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeAtLowBandForTopScore);
		assertEquals(TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueAndTimeAtHighBandForTopScore() {
		int servicedNumber = 10;
		int entryTimeAtLowBandForTopScore = 
				servicedNumber * AVERAGE_SERVICE_DUATION;		
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeAtLowBandForTopScore);
		assertEquals(TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE, actualEstimation);
	}
	
	@Test
	public void testWhenEntryTimeBeforeOpeningHour() {
		int servicedNumber = 1;
		int entryTimeBeforeOpeningHour = OPENING_TIME - 1;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeBeforeOpeningHour);;
		assertEquals(TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE, actualEstimation);
	}

	@Test
	public void testWhenEntryTimeAfterOpeningHour() {
		int servicedNumber = 1;
		int entryTimeBeforeOpeningHour = CLOSING_TIME + 1;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTimeBeforeOpeningHour);;
		assertEquals(TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueLowerThenExpectedValue() {
		int servicedNumber = 8;
		int entryTime = 2 * servicedNumber * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);;
		assertTrue(actualEstimation > TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE);
		assertTrue(actualEstimation < TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE);
		assertEquals(84, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueHigherThenExpectedValue() {
		int servicedNumber = 10;
		int entryTime = (servicedNumber / 2 ) * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);
		assertTrue(actualEstimation > TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE);
		assertTrue(actualEstimation < TimeBasedInputQualityEstimatorImpl.MAX_QUALITY_SCORE);
		assertEquals(94, actualEstimation);
	}
	
	@Test
	public void testWhenEntryValueOutOfTheAcceptedRange() {
		int servicedNumber = 20;
		int entryTime = (servicedNumber + 26) * AVERAGE_SERVICE_DUATION;
		int actualEstimation = estimateQualityWrapper(
				servicedNumber, entryTime);
		assertEquals(TimeBasedInputQualityEstimatorImpl.MIN_QUALITY_SCORE, actualEstimation);
	}
}
