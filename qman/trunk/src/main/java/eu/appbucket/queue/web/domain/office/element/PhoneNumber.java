package eu.appbucket.queue.web.domain.office.element;


public class PhoneNumber {
	  
	private String countryCode;
	private String areaCode;
	private String lineNumber;
	private String extension;
	  
	public String getCountryCode() {
		return countryCode;
	}
	public void setCountryCode(String phoneCountryCode) {
		this.countryCode = phoneCountryCode;
	}
	public String getAreaCode() {
		return areaCode;
	}
	public void setAreaCode(String phoneAreaCode) {
		this.areaCode = phoneAreaCode;
	}
	public String getLineNumber() {
		return lineNumber;
	}
	public void setLineNumber(String phoneLineNumber) {
		this.lineNumber = phoneLineNumber;
	}
	public String getExtension() {
		return extension;
	}
	public void setExtension(String phoneExtension) {
		this.extension = phoneExtension;
	}
	
	public static PhoneNumber fromPhoneNumber(eu.appbucket.queue.core.domain.queue.PhoneNumber phoneNumberInput) {
		PhoneNumber phoneNumber = new PhoneNumber();
		phoneNumber.setCountryCode(phoneNumberInput.getCountryCode());
		phoneNumber.setAreaCode(phoneNumberInput.getAreaCode());
		phoneNumber.setLineNumber(phoneNumberInput.getLineNumber());
		phoneNumber.setExtension(phoneNumberInput.getExtension());
		return phoneNumber;
	} 
}
