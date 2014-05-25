package eu.appbucket.queue.core.domain.queue;

public class QueueInfo {
	
	private int queueId;
	private String name;

	public int getQueueId() {
		return queueId;
	}
	
	public void setQueueId(int queueId) {
		this.queueId = queueId;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + queueId;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		QueueInfo other = (QueueInfo) obj;
		if (queueId != other.queueId)
			return false;
		return true;
	}
}
