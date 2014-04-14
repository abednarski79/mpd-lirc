package eu.appbucket.queue.web.domain.office.element;

public class OpeningHours {

	private int openingHour;
	private int openingMinute;
	private int closingHour;
	private int closingMinute;
	
	public int getOpeningHour() {
		return openingHour;
	}
	public void setOpeningHour(int openingHour) {
		this.openingHour = openingHour;
	}
	public int getOpeningMinute() {
		return openingMinute;
	}
	public void setOpeningMinute(int openingMinute) {
		this.openingMinute = openingMinute;
	}
	public int getClosingHour() {
		return closingHour;
	}
	public void setClosingHour(int closingHour) {
		this.closingHour = closingHour;
	}
	public int getClosingMinute() {
		return closingMinute;
	}
	public void setClosingMinute(int closingMinute) {
		this.closingMinute = closingMinute;
	}
	
	public static OpeningHours fromOpeningHours(eu.appbucket.queue.core.domain.queue.OpeningHours openingHoursInput) {
		OpeningHours openingHours = new OpeningHours();
		openingHours.setOpeningHour(openingHoursInput.getOpeningHour());
		openingHours.setOpeningMinute(openingHoursInput.getOpeningMinute());
		openingHours.setClosingHour(openingHoursInput.getClosingHour());
		openingHours.setClosingMinute(openingHoursInput.getClosingMinute());
		return openingHours;
	}
}
