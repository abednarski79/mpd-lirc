package eu.appbucket.queue.web.domain.office.element;

import eu.appbucket.queue.core.domain.queue.QueueDetails;

public class ContactDetails {
	
	private PhoneNumber phoneNumber;
	private String email;
	private String website;
	
	public PhoneNumber getPhoneNumber() {
		return phoneNumber;
	}
	public void setPhoneNumber(PhoneNumber phoneNumber) {
		this.phoneNumber = phoneNumber;
	}
	public String getWebsite() {
		return website;
	}
	public void setWebsite(String website) {
		this.website = website;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
	public static ContactDetails fromQueueDetails(QueueDetails queuDetails) {
		ContactDetails contactDetails = new ContactDetails();
		contactDetails.setEmail(queuDetails.getEmail());
		PhoneNumber phoneNumber = PhoneNumber.fromPhoneNumber(queuDetails.getPhoneNumber());
		contactDetails.setPhoneNumber(phoneNumber);
		contactDetails.setWebsite(queuDetails.getWebsite());
		return contactDetails;
	}
}
