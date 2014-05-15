package eu.appbucket.queue.core.domain.queue;


/**
 * Static set of information about the queue.
 */
public class QueueDetails {
	
	private GeographicalLocation location;
	private String phoneNumber;
	private String email;
	private Address address;
	private OpeningHours openingHoursLocalTimeZone;
	private OpeningHours openingHoursUTC;
	private OpeningTimes openingTimesUTC;	
	private int defaultAverageWaitingDuration;
	
	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
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

	public OpeningTimes getOpeningTimesUTC() {
		return openingTimesUTC;
	}

	public void setOpeningTimesUTC(OpeningTimes openingTimesUTC) {
		this.openingTimesUTC = openingTimesUTC;
	}

	public GeographicalLocation getLocation() {
		return location;
	}

	public void setLocation(GeographicalLocation location) {
		this.location = location;
	}

	public String getPhoneNumber() {
		return phoneNumber;
	}

	public void setPhoneNumber(String phoneNumber) {
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
}
