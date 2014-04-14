package eu.appbucket.queue.core.domain.queue;

import java.util.Date;

public class OpeningTimes {

	private long openingTime;
	private long closingTime;

	public long getOpeningTime() {
		return openingTime;
	}

	public void setOpeningTime(long openingTime) {
		this.openingTime = openingTime;
	}

	public long getClosingTime() {
		return closingTime;
	}

	public void setClosingTime(long closingTime) {
		this.closingTime = closingTime;
	}

	@Override
	public String toString() {
		return "OpeningTime [openingTime=" + new Date(openingTime) + ", closingTime="
				+ new Date(closingTime) + "]";
	}
}
