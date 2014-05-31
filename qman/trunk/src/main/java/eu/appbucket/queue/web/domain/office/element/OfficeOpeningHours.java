package eu.appbucket.queue.web.domain.office.element;

import java.util.Collection;
import java.util.HashSet;

import eu.appbucket.queue.core.domain.queue.Openings;

public class OfficeOpeningHours {
	
	private Collection<DailyOpeningHours> openingHoursByWeekdays = new HashSet<DailyOpeningHours>();
	
	void addOpeningHours(DailyOpeningHours openingHours) {
		this.openingHoursByWeekdays.add(openingHours);
	}
	
	public Collection<DailyOpeningHours> getOpeningHoursByWeekdays() {
		return openingHoursByWeekdays;
	}
	
	public static OfficeOpeningHours fromOpenings(
			Collection<Openings> openings) {
		OfficeOpeningHours officeOpeningHours = new OfficeOpeningHours();
		for(Openings dailyOpenings: openings) {
			officeOpeningHours.addOpeningHours(DailyOpeningHours.fromDailyOpenings(dailyOpenings));
		}
		return officeOpeningHours;
	}
}
