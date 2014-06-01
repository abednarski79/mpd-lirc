package eu.appbucket.queue.web.domain.office;

import java.util.Collection;
import java.util.HashSet;

import eu.appbucket.queue.core.domain.queue.Openings;
import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.web.domain.office.element.Address;
import eu.appbucket.queue.web.domain.office.element.ContactDetails;
import eu.appbucket.queue.web.domain.office.element.DailyOpeningHours;
import eu.appbucket.queue.web.domain.office.element.GeographicalLocation;

public class OfficeDetails {	
	
	private Address address;
	private Collection<DailyOpeningHours> openingHours; // = new HashSet<DailyOpeningHours>();
	private ContactDetails contactDetails;
	private String description; 
	private GeographicalLocation location;
	
	public GeographicalLocation getLocation() {
		return location;
	}
	public void setLocation(GeographicalLocation location) {
		this.location = location;
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
	public Collection<DailyOpeningHours> getOpeningHours() {
		return openingHours;
	}
	public void setOpeningHours(Collection<DailyOpeningHours> openingHours) {
		this.openingHours = openingHours;
	}
	public ContactDetails getContactDetails() {
		return contactDetails;
	}
	public void setContactDetails(ContactDetails contactDetails) {
		this.contactDetails = contactDetails;
	}
	
	public static OfficeDetails fromQueueData(
			QueueInfo queueInfo, QueueDetails queueDetails) {
		OfficeDetails officeDetails = new OfficeDetails();
		Address address = Address.fromQueuInfoAndAddress(queueInfo, queueDetails, queueDetails.getAddress());		
		officeDetails.setAddress(address);
		ContactDetails contactDetails = ContactDetails.fromQueueDetails(queueDetails);
		officeDetails.setContactDetails(contactDetails);
		officeDetails.setDescription(queueDetails.getDescription());
		Collection<DailyOpeningHours> openingHours = new HashSet<DailyOpeningHours>();
		for(Openings dailyOpenings: queueDetails.getOpenings().values()) {
			openingHours.add(DailyOpeningHours.fromDailyOpenings(dailyOpenings));
		}
		officeDetails.setOpeningHours(openingHours);
		GeographicalLocation location = GeographicalLocation.fromGeographicalLocation(queueDetails.getLocation());
		officeDetails.setLocation(location);
		return officeDetails;
	}
}