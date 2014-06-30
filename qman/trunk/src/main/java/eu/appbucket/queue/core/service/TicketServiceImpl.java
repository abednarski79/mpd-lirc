package eu.appbucket.queue.core.service;

import java.util.Collection;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;
import eu.appbucket.queue.core.persistence.TicketDao;
import eu.appbucket.queue.core.service.estimator.duration.WaitingTimeEsimationStrategy;
import eu.appbucket.queue.core.service.estimator.duration.WaitingTimeEstimatorStrategyFactory;
import eu.appbucket.queue.core.service.estimator.quality.TimeBasedInputQualityEstimator;
import eu.appbucket.queue.core.service.util.TimeGenerator;

@Service
public class TicketServiceImpl implements TicketService {
	
	private TicketDao ticketDao;
	private QueueService queueService;
	private WaitingTimeEstimatorStrategyFactory waitingTimeEstimatorStrategyFactory;
	private TimeBasedInputQualityEstimator timeBasedInputQualityEstimator;
	private static final int MINIMUM_TICKET_UPDATES_TO_CALCULATE_AVERAGE = 5;
	private static final int MINIMUM_ACCEPTED_INPUT_QUALITY = 1;
	
	@Autowired
	public void setTimeBasedInputQualityEstimator(
			TimeBasedInputQualityEstimator timeBasedInputQualityEstimator) {
		this.timeBasedInputQualityEstimator = timeBasedInputQualityEstimator;
	}

	@Autowired
	public void setTicketDao(TicketDao ticketDao) {
		this.ticketDao = ticketDao;
	}
	
	@Autowired
	public void setQueueService(QueueService queueService) {
		this.queueService = queueService;
	}
	
	@Autowired
	public void setWaitingTimeEstimatorStrategyFactory(
			WaitingTimeEstimatorStrategyFactory waitingTimeEstimatorStrategyFactory) {
		this.waitingTimeEstimatorStrategyFactory = waitingTimeEstimatorStrategyFactory;
	}
	
	public TicketEstimation getTicketEstimation(QueueDetails queueDetails, QueueStats queueStats, int ticketId) {
		WaitingTimeEsimationStrategy estimatorStrategy = waitingTimeEstimatorStrategyFactory.getStrategy(queueStats);
		TicketEstimation ticketEstimation = estimatorStrategy.estimateTimeToBeServiced(queueDetails, queueStats, ticketId);
		return ticketEstimation;
	}
	
	public void processTicketInformation(TicketUpdate ticketUpdate) {
		processAndStoreTicketUpdate(ticketUpdate);
		recalculateQueueAndStoreAverageServiceDuration(ticketUpdate);
	}
	
	private void processAndStoreTicketUpdate(TicketUpdate ticketUpdate) {
		QueueDetails queueDetails =  queueService.getQueueDetailsByQueueId(ticketUpdate.getQueueInfo().getQueueId());
		QueueStats queueStats = queueService.getQueueStatsByQueueId(ticketUpdate.getQueueInfo().getQueueId()); 
		ticketUpdate.setQuality(timeBasedInputQualityEstimator.estimateInputQuality(queueDetails, queueStats, ticketUpdate));
		ticketDao.storeTicketUpdate(ticketUpdate);
		if(isTicketQualityAcceptable(ticketUpdate) && isTicketHigherThenHighestTicketFromToday(ticketUpdate)) {
			ticketDao.cleanHighestTicketUpdateByQueueAndDayCache(ticketUpdate.getQueueInfo());
		}
	}
	
	private boolean isTicketQualityAcceptable(TicketUpdate ticketUpdate) {
		if(ticketUpdate.getQuality() >= MINIMUM_ACCEPTED_INPUT_QUALITY) {
			return true;
		}
		return false;
	}
	
	private boolean isTicketHigherThenHighestTicketFromToday(TicketUpdate ticketUpdate) {
		int ticketNumber = ticketUpdate.getCurrentlyServicedTicketNumber();
		int highetTicketNumber = getHighestTicketUpdatesFromToday(ticketUpdate.getQueueInfo()).getCurrentlyServicedTicketNumber();
		if(ticketNumber > highetTicketNumber) {
			return true;
		}
		return false;
	}
	
	private void recalculateQueueAndStoreAverageServiceDuration(TicketUpdate ticketUpdate) {
		if(!isTicketQualityAcceptable(ticketUpdate)) {
			return;
		}
		QueueInfo queueInfo = ticketUpdate.getQueueInfo();		
		Collection<TicketUpdate> ticketUpdatesFromToday = getTicketUpdatesFromToday(queueInfo);
		if(hasMinimumRequiredNumberOfUpdates(ticketUpdatesFromToday)) {
			int ticketAverageServiceDuration = getTicketAverageServiceDuration(ticketUpdatesFromToday, queueInfo);
			updateTodaysQueueAverageServiceDuration(ticketAverageServiceDuration, queueInfo);
		}
	}
	
	private boolean hasMinimumRequiredNumberOfUpdates(Collection<TicketUpdate> ticketUpdatesFromToday) {
		if(ticketUpdatesFromToday.size() >= MINIMUM_TICKET_UPDATES_TO_CALCULATE_AVERAGE) {
			return true;
		}
		return false;
	}
	private Collection<TicketUpdate> getTicketUpdatesFromToday(QueueInfo queueInfo) {
		int queueId = queueInfo.getQueueId();
		Date queueOpeningTime = getQueueOpeningTimeByQueueId(queueId);
		Date queueClosingTime = getQueueClosingTimeByQueueId(queueId);		
		Collection<TicketUpdate> todayTicketUpdates = 
				ticketDao.readTicketUpdatesByQueueAndDate(
						queueInfo, 
						queueOpeningTime, queueClosingTime,
						MINIMUM_ACCEPTED_INPUT_QUALITY);
		return todayTicketUpdates;
	}
	
	private Date getQueueOpeningTimeByQueueId(int queueId) {
		QueueDetails  queueDetails  = queueService.getQueueDetailsByQueueId(queueId);
		Date queueOpeningTime = new Date(queueDetails.getTodayOpeningTimesUTC().getOpeningTime());
		return queueOpeningTime;
	}
	
	private Date getQueueClosingTimeByQueueId(int queueId) {
		QueueDetails  queueDetails  = queueService.getQueueDetailsByQueueId(queueId);
		Date queueClosingTime = new Date(queueDetails.getTodayOpeningTimesUTC().getClosingTime());
		return queueClosingTime;
	}
		
	private int getTicketAverageServiceDuration(Collection<TicketUpdate> todayTicketUpdates, QueueInfo queueInfo) {				
		Map<Integer, Set<TicketUpdate>> ticketNumberToUpdates = groupUpdatesForPerTicket(todayTicketUpdates);				
		Set<Integer> averageServiceDurations = calculateAverageServiceDurations(ticketNumberToUpdates, queueInfo);
		int overallAverageServiceTime = calculateOverallAverageServiceDuration(averageServiceDurations);
		return overallAverageServiceTime;
	}
	
	protected Map<Integer, Set<TicketUpdate>> groupUpdatesForPerTicket(Collection<TicketUpdate> ticketUpdates) {
		Map<Integer, Set<TicketUpdate>> ticketNumberToUpdates = new HashMap<Integer, Set<TicketUpdate>>();		
		for(TicketUpdate ticketUpdate: ticketUpdates) {
			ticketNumberToUpdates = storeTicketUpdate(ticketUpdate, ticketNumberToUpdates);
		}
		return ticketNumberToUpdates;
	}
	
	private Map<Integer, Set<TicketUpdate>> storeTicketUpdate(
			TicketUpdate ticketUpdateToStore, Map<Integer, Set<TicketUpdate>> ticketNumberToUpdates) {
		int ticketNumber = ticketUpdateToStore.getCurrentlyServicedTicketNumber();
		if(!ticketNumberToUpdates.containsKey(ticketNumber)) {
			ticketNumberToUpdates.put(ticketNumber, new HashSet<TicketUpdate>());
		}
		ticketNumberToUpdates.get(ticketNumber).add(ticketUpdateToStore);
		return ticketNumberToUpdates;
	}
	
	protected Set<Integer> calculateAverageServiceDurations(
			Map<Integer, Set<TicketUpdate>> ticketNumberToUpdates,
			QueueInfo queueInfo) {
		Set<Integer> averageServiceDurations = new HashSet<Integer>();
		Set<Integer> averageTicketServiceDurationsPerTicket = new HashSet<Integer>();
		Set<Integer> ticketNumbers = ticketNumberToUpdates.keySet();
		Set<TicketUpdate> updatesPerTicket;
		Date queueOpeningTime = getQueueOpeningTimeByQueueId(queueInfo.getQueueId());
		for(int ticketNumber: ticketNumbers) {
			averageTicketServiceDurationsPerTicket.clear();
			updatesPerTicket = ticketNumberToUpdates.get(ticketNumber);
			for(TicketUpdate ticketUpdate: updatesPerTicket) {				
				long offsetFromQueueOpeningToUpdateTime = ticketUpdate.getCreated().getTime() - queueOpeningTime.getTime();
				int averageTicketServiceDurationForUpdate = (int) offsetFromQueueOpeningToUpdateTime / ticketNumber;
				averageTicketServiceDurationsPerTicket.add(averageTicketServiceDurationForUpdate);
			}
			int totalAverageServiceDuration = 0;
			for(int averageServiceDuration: averageTicketServiceDurationsPerTicket) {
				totalAverageServiceDuration += averageServiceDuration;
			}
			int averageServiceDuration = totalAverageServiceDuration / averageTicketServiceDurationsPerTicket.size();
			averageServiceDurations.add(averageServiceDuration);
		}
		return averageServiceDurations;
	}
	
	protected int calculateOverallAverageServiceDuration(Set<Integer> averageServiceDurations) {
		int totalAverageServiceDuration = 0;
		for(int averageServiceDuration: averageServiceDurations) {
			totalAverageServiceDuration += averageServiceDuration;
		}
		int overallAverageServiceDuration = totalAverageServiceDuration / averageServiceDurations.size();
		return overallAverageServiceDuration;
	}
	
	private void updateTodaysQueueAverageServiceDuration(int ticketAverageServiceDuration, QueueInfo queueInfo) {		
		QueueStats queueStats = queueService.getQueueStatsByQueueId(queueInfo.getQueueId());
		Date todayAtMidnight = TimeGenerator.getTodayMidnightDate();
		queueStats.setDate(todayAtMidnight);
		queueStats.setCalculatedAverageWaitingDuration(ticketAverageServiceDuration);		
		queueService.updateQueueStats(queueStats);
	}

	public TicketUpdate getHighestTicketUpdatesFromToday(QueueInfo queueInfo) {
		int queueId = queueInfo.getQueueId();
		Date queueOpeningTime = getQueueOpeningTimeByQueueId(queueId);
		Date queueClosingTime = getQueueClosingTimeByQueueId(queueId);		
		TicketUpdate highestTicketUpdates = ticketDao.readHighestTicketUpdateByQueueAndDay(
				queueInfo, queueOpeningTime, queueClosingTime, MINIMUM_ACCEPTED_INPUT_QUALITY);
		return highestTicketUpdates;
	}
}
