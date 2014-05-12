package eu.appbucket.queue.core.service.util;

import java.util.Calendar;
import java.util.Date;

public class TimeGenerator {
	
	public static Date getTodayMidnightDate() {
		Date now = new Date();
		Calendar calendar = Calendar.getInstance();
		calendar.setTime(now);
		calendar.set(Calendar.HOUR_OF_DAY, 0);
		calendar.set(Calendar.MINUTE, 0);
		calendar.set(Calendar.SECOND, 0);
		calendar.set(Calendar.MILLISECOND, 0);
		return calendar.getTime();
	}
}
