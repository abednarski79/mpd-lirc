package eu.appbucket.queue.web.domain.office.element;

import java.util.HashMap;
import java.util.Map;

import org.joda.time.DateTimeConstants;

import eu.appbucket.queue.core.domain.queue.Openings;

public class DailyOpeningHours {

	private static Map<Integer, String> dayIdToDayName;
	
	static {
		dayIdToDayName = new HashMap<Integer, String>();
		dayIdToDayName.put(DateTimeConstants.MONDAY, "MONDAY");
		dayIdToDayName.put(DateTimeConstants.TUESDAY, "TUESDAY");
		dayIdToDayName.put(DateTimeConstants.WEDNESDAY, "WEDNESDAY");
		dayIdToDayName.put(DateTimeConstants.THURSDAY, "THURSDAY");
		dayIdToDayName.put(DateTimeConstants.FRIDAY, "FRIDAY");
		dayIdToDayName.put(DateTimeConstants.SATURDAY, "SATURDAY");
		dayIdToDayName.put(DateTimeConstants.SUNDAY, "SUNDAY");
	}
	
	private String day;
	private int id;
	private int openingHour;
	private int openingMinute;
	private int closingHour;
	private int closingMinute;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getDay() {
		return day;
	}
	public void setDay(String day) {
		this.day = day;
	}
	public int getOpeningHour() {
		return openingHour;
	}
	public void setOpeningHour(int openingHour) {
		this.openingHour = openingHour;
	}
	public int getOpeningMinute() {
		return openingMinute;
	}
	public void setOpeningMinute(int openingMinute) {
		this.openingMinute = openingMinute;
	}
	public int getClosingHour() {
		return closingHour;
	}
	public void setClosingHour(int closingHour) {
		this.closingHour = closingHour;
	}
	public int getClosingMinute() {
		return closingMinute;
	}
	public void setClosingMinute(int closingMinute) {
		this.closingMinute = closingMinute;
	}
	
	public static DailyOpeningHours fromDailyOpenings(Openings dailyOpenings) {
		DailyOpeningHours openingHours = new DailyOpeningHours();
		openingHours.setId(dailyOpenings.getDayId());
		openingHours.setDay(dayIdToDayName.get(dailyOpenings.getDayId()));		
		openingHours.setOpeningHour(dailyOpenings.getOpeningHoursLocalTimeZone().getOpeningHour());
		openingHours.setOpeningMinute(dailyOpenings.getOpeningHoursLocalTimeZone().getOpeningMinute());
		openingHours.setClosingHour(dailyOpenings.getOpeningHoursLocalTimeZone().getClosingHour());
		openingHours.setClosingMinute(dailyOpenings.getOpeningHoursLocalTimeZone().getClosingMinute());
		return openingHours;
	}
}
