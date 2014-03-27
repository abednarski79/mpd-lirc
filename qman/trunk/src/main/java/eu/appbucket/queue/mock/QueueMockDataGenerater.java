package eu.appbucket.queue.mock;

import java.util.Random;

import eu.appbucket.queue.domain.queue.Address;
import eu.appbucket.queue.domain.queue.GeographicalLocation;
import eu.appbucket.queue.domain.queue.OpeningHours;
import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueStats;

public class QueueMockDataGenerater {
	
	public static QueueStats generateMockQueueStats() {
		QueueStats queueStats = new QueueStats();
		Random randomGenerator = new Random();		
		queueStats.setAverageWaitingTimeInSeconds(randomGenerator.nextInt(3600));		
		queueStats.setHighestGivenTicketNumber(randomGenerator.nextInt(200));
		return queueStats;
	}
	
	public static QueueDetails generateMockQueueDetails() {
		QueueDetails queueDetails = new QueueDetails();		
		Address address = new Address();
		address.setAddressLine1("Adress line 1");
		address.setAddressLine2("Adress line 2");
		address.setCountry("Republic Of Irlenad");
		address.setCounty("Dublin");
		address.setPostcode("D1");
		address.setTownOrCity("Dublin");
		queueDetails.setAddress(address);
		GeographicalLocation location = new GeographicalLocation();
		location.setLatitude(53.347778F);
		location.setLongitude(-6.259722F);
		queueDetails.setLocation(location);
		OpeningHours openingHours = new OpeningHours();
		openingHours.setOpeningHour(8);
		openingHours.setOpeningMinute(30);
		openingHours.setClosingHour(17);
		openingHours.setOpeningMinute(30);
		queueDetails.setOpeningHours(openingHours);
		queueDetails.setPhoneNumber("016669100");
		queueDetails.setEmail("gnib_dv@garda.ie");
		return queueDetails;
	}
}
