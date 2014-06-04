package eu.appbucket.queue.core.domain.queue;

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
}
