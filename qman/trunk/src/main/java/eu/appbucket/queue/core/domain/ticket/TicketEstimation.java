package eu.appbucket.queue.core.domain.ticket;

public class TicketEstimation {	
		
	private long serviceTime;
	
	public long getServiceTime() {
		return serviceTime;
	}
	public void setServiceTime(long serviceTime) {
		this.serviceTime = serviceTime;
	}
	
	@Override
	public String toString() {
		return "TicketStatus [serviceTime=" + serviceTime + "]";
	}	
}
