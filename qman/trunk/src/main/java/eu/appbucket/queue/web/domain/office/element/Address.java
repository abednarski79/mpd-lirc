package eu.appbucket.queue.web.domain.office.element;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;

public class Address {
	
	private String name;
	private String addressLine1;
	private String addressLine2;
	private String townOrCity;
	private String county;
	private String postcode;
	private String country;

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAddressLine1() {
		return addressLine1;
	}
	public void setAddressLine1(String addressLine1) {
		this.addressLine1 = addressLine1;
	}
	public String getAddressLine2() {
		return addressLine2;
	}
	public void setAddressLine2(String addressLine2) {
		this.addressLine2 = addressLine2;
	}
	public String getTownOrCity() {
		return townOrCity;
	}
	public void setTownOrCity(String townOrCity) {
		this.townOrCity = townOrCity;
	}
	public String getCounty() {
		return county;
	}
	public void setCounty(String county) {
		this.county = county;
	}
	public String getPostcode() {
		return postcode;
	}
	public void setPostcode(String postcode) {
		this.postcode = postcode;
	}
	public String getCountry() {
		return country;
	}
	public void setCountry(String country) {
		this.country = country;
	}
	
	public static Address fromQueuInfoAndAddress(QueueInfo queueInfo, QueueDetails queueDetails,
			eu.appbucket.queue.core.domain.queue.Address addressInput) {
		Address address = new Address();
		address.setName(queueDetails.getName());
		address.setAddressLine1(addressInput.getAddressLine1());
		address.setAddressLine2(addressInput.getAddressLine2());
		address.setCountry(addressInput.getCountry());
		address.setCounty(addressInput.getCounty());
		address.setPostcode(addressInput.getPostcode());
		address.setTownOrCity(addressInput.getTownOrCity());
		return address;
	}
}
