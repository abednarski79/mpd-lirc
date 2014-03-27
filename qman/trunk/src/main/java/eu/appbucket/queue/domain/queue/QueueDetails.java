package eu.appbucket.queue.domain.queue;

/**
 * Static set of information about the queue.
 */
public class QueueDetails {

	private OpeningHours openingHours;
	private GeographicalLocation location;
	private String phoneNumber;
	private String email;
	private Address address;
	
	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	public OpeningHours getOpeningHours() {
		return openingHours;
	}

	public void setOpeningHours(OpeningHours openingHours) {
		this.openingHours = openingHours;
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

	@Override
	public String toString() {
		return "QueueDetails [openingHours=" + openingHours + ", location="
				+ location + ", phoneNumber=" + phoneNumber + ", email="
				+ email + ", address=" + address + "]";
	}
}
