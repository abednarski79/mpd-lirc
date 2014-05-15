package eu.appbucket.queue.web.domain.office;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.web.domain.office.element.Address;
import eu.appbucket.queue.web.domain.office.element.ContactDetails;
import eu.appbucket.queue.web.domain.office.element.OpeningHours;
import eu.appbucket.queue.web.domain.office.element.Stats;


public class OfficeDetails {	
	
	private Address address;
	private OpeningHours openingHours;	
	private ContactDetails contactDetails;
	private Stats stats;
	
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
	public ContactDetails getContactDetails() {
		return contactDetails;
	}
	public void setContactDetails(ContactDetails contactDetails) {
		this.contactDetails = contactDetails;
	}
	public Stats getStats() {
		return stats;
	}
	public void setStats(Stats stats) {
		this.stats = stats;
	}
	
	public static OfficeDetails fromQueueData(QueueInfo queueInfo, QueueDetails queueDetails, QueueStats queueStats) {
		OfficeDetails officeDetails = new OfficeDetails();
		Address address = Address.fromQueuInfoAndAddress(queueInfo, queueDetails.getAddress());		
		officeDetails.setAddress(address);
		ContactDetails contactDetails = ContactDetails.fromQueueDetails(queueDetails);
		officeDetails.setContactDetails(contactDetails);
		OpeningHours openingHours = OpeningHours.fromOpeningHours(queueDetails.getOpeningHoursLocalTimeZone());
		officeDetails.setOpeningHours(openingHours);
		Stats stats = Stats.fromQueueDetailsAndStats(queueDetails, queueStats);
		officeDetails.setStats(stats);
		return officeDetails;
		
	}
}