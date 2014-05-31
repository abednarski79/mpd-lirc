package eu.appbucket.queue.core.domain.queue;

import java.util.Map;

public class QueueOpeningHours {
	
	private Map<Integer, OpeningHours> openingHoursLocalTimeZone;
	private Map<Integer, OpeningHours> openingHoursUTC;
	private Map<Integer, OpeningTimes> openingTimesUTC;
	
	public void addOpeningHoursLocalTimeZone(int dayId, OpeningHours openingHours) {
		openingHoursLocalTimeZone.put(dayId, openingHours);
	}
	
	public void addOpeningHoursUTC(int dayId, OpeningHours openingHours) {
		openingHoursUTC.put(dayId, openingHours);
	}
	
	void addOpeningTimesUTC(int dayId, OpeningTimes openingTimes) {
		openingTimesUTC.put(dayId, openingTimes);
	}
	
	public Map<Integer, OpeningHours> getOpeningHoursLocalTimeZone() {
		return openingHoursLocalTimeZone;
	}

	public Map<Integer, OpeningHours> getOpeningHoursUTC() {
		return openingHoursUTC;
	}

	public Map<Integer, OpeningTimes> getOpeningTimesUTC() {
		return openingTimesUTC;
	}
}
