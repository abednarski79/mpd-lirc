package eu.appbucket.queue.domain.ticket;

public class TicketStats {	
		
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
