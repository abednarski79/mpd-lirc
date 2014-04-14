package eu.appbucket.queue.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueStats;
import eu.appbucket.queue.core.domain.ticket.TicketEstimation;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;
import eu.appbucket.queue.core.persistence.TicketDao;
import eu.appbucket.queue.core.service.estimator.BasicWaitingTimeEsimationStraregyImpl;
import eu.appbucket.queue.core.service.estimator.WaitingTimeEsimationStraregy;

@Service
public class TicketServiceImpl implements TicketService {
	
	private TicketDao ticketDao;
	
	@Autowired
	public void setTicketDao(TicketDao ticketDao) {
		this.ticketDao = ticketDao;
	}
	
	public TicketEstimation getTicketEstimation(QueueDetails queueDetails, QueueStats queueStats, int ticketId) {
		WaitingTimeEsimationStraregy estimatorStrategy = new BasicWaitingTimeEsimationStraregyImpl();
		TicketEstimation ticketEstimation = estimatorStrategy.estimateWaitingTime(queueDetails, queueStats, ticketId);
		return ticketEstimation;
	}
	
	public void processTicketInformation(TicketUpdate ticketUpdate) {
		ticketDao.storeTicketUpdate(ticketUpdate);
		// read all entries for today
		// recalculate queue avarage
		// update queue average
	}
}
