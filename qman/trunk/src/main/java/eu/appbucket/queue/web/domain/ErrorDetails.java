package eu.appbucket.queue.web.domain;

public class ErrorDetails {
	
	private int status;
	private int code;
	private String message;
	private String developerMessage;
	private String moreInfo;
	
	public int getStatus() {
		return status;
	}
	public void setStatus(int status) {
		this.status = status;
	}
	public int getCode() {
		return code;
	}
	public void setCode(int code) {
		this.code = code;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	public String getDeveloperMessage() {
		return developerMessage;
	}
	public void setDeveloperMessage(String developerMessage) {
		this.developerMessage = developerMessage;
	}
	public String getMoreInfo() {
		return moreInfo;
	}
	public void setMoreInfo(String moreInfo) {
		this.moreInfo = moreInfo;
	}
}
