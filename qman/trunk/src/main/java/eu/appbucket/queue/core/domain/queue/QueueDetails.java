package eu.appbucket.queue.core.domain.queue;

import java.util.Calendar;
import java.util.Map;


/**
 * Static set of information about the queue.
 */
public class QueueDetails {
	
	private String name;
	private String description;
	private GeographicalLocation location;
	private PhoneNumber phoneNumber;
	private String email;
	private Address address;
	private Map<Integer, Openings>  openings;
	private int defaultAverageWaitingDuration;
	private String website;
	
	public OpeningTimes getTodayOpeningTimesUTC() {
		int todayId = getTodayId();
		if(!openings.containsKey(todayId)) {
			return new OpeningTimes();
		}
		OpeningHours todayOpeningHoursUTC = openings.get(todayId).getOpeningHoursUTC();
		OpeningTimes todayOpeningTimesUTC = calculateOpeningTimeUTC(todayOpeningHoursUTC);
		return todayOpeningTimesUTC;
	}
	
	protected int getTodayId() {
		int todayId = Calendar.getInstance().get(Calendar.DAY_OF_WEEK);
		return todayId;
	}
	
	protected OpeningTimes calculateOpeningTimeUTC(OpeningHours openingHours) {
		OpeningTimes openingTime = new OpeningTimes();
		Calendar calendar = Calendar.getInstance();		
		calendar.set(Calendar.HOUR_OF_DAY, openingHours.getOpeningHour());
		calendar.set(Calendar.MINUTE, openingHours.getOpeningMinute());			
		calendar.set(Calendar.SECOND, 0);
		calendar.set(Calendar.MILLISECOND, 0);
		openingTime.setOpeningTime(calendar.getTimeInMillis());
		calendar.set(Calendar.HOUR_OF_DAY, openingHours.getClosingHour());
		calendar.set(Calendar.MINUTE, openingHours.getClosingMinute());
		calendar.set(Calendar.SECOND, 0);
		calendar.set(Calendar.MILLISECOND, 0);
		openingTime.setClosingTime(calendar.getTimeInMillis());			
		return openingTime;
	}
	
	public Map<Integer, Openings> getOpenings() {
		return openings;
	}
	
	public void setOpenings(Map<Integer, Openings> openings) {
		this.openings = openings;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	public GeographicalLocation getLocation() {
		return location;
	}

	public void setLocation(GeographicalLocation location) {
		this.location = location;
	}

	public PhoneNumber getPhoneNumber() {
		return phoneNumber;
	}

	public void setPhoneNumber(PhoneNumber phoneNumber) {
		this.phoneNumber = phoneNumber;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public int getDefaultAverageWaitingDuration() {
		return defaultAverageWaitingDuration;
	}

	public void setDefaultAverageWaitingDuration(int defaultAverageWaitingDuration) {
		this.defaultAverageWaitingDuration = defaultAverageWaitingDuration;
	}

	public String getWebsite() {
		return website;
	}

	public void setWebsite(String website) {
		this.website = website;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
}
