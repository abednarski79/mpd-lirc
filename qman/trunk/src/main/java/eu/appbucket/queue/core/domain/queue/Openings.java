package eu.appbucket.queue.core.domain.queue;

public class Openings {
	
	private int dayId;
	private OpeningHours openingHoursLocalTimeZone;
	private OpeningHours openingHoursUTC;
	/*private OpeningTimes openingTimesUTC;*/

	public int getDayId() {
		return dayId;
	}
	public void setDayId(int dayId) {
		this.dayId = dayId;
	}
	public OpeningHours getOpeningHoursLocalTimeZone() {
		return openingHoursLocalTimeZone;
	}
	public void setOpeningHoursLocalTimeZone(OpeningHours openingHoursLocalTimeZone) {
		this.openingHoursLocalTimeZone = openingHoursLocalTimeZone;
	}
	public OpeningHours getOpeningHoursUTC() {
		return openingHoursUTC;
	}
	public void setOpeningHoursUTC(OpeningHours openingHoursUTC) {
		this.openingHoursUTC = openingHoursUTC;
	}
	/*public OpeningTimes getOpeningTimesUTC() {
		return openingTimesUTC;
	}
	public void setOpeningTimesUTC(OpeningTimes openingTimesUTC) {
		this.openingTimesUTC = openingTimesUTC;
	}*/
}
