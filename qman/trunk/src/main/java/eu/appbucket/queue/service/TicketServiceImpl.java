package eu.appbucket.queue.service;

import org.springframework.stereotype.Service;

import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueStats;
import eu.appbucket.queue.domain.ticket.TicketStats;
import eu.appbucket.queue.domain.ticket.TicketUpdate;
import eu.appbucket.queue.service.estimator.BasicWaitingTimeEsimationStraregyImpl;
import eu.appbucket.queue.service.estimator.WaitingTimeEsimationStraregy;

@Service
public class TicketServiceImpl implements TicketService {
	
	public TicketStats getTicketStatistics(QueueDetails queueDetails, QueueStats queueStats, int ticketId) {
		WaitingTimeEsimationStraregy estimatorStrategy = new BasicWaitingTimeEsimationStraregyImpl();
		TicketStats ticketStatus = estimatorStrategy.estimateWaitingTime(queueDetails, queueStats, ticketId);
		return ticketStatus;
	}
	
	public void updateTicketInformation(TicketUpdate ticketUpdate) {
		// TODO: persist ticketUpdate in DB		
	}
}
