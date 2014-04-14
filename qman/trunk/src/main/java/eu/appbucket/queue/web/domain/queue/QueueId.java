package eu.appbucket.queue.web.domain.queue;

import eu.appbucket.queue.core.domain.queue.QueueInfo;

public class QueueId {
	
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
	
	public static QueueId fromQueueInfo(QueueInfo queueInfo) {
		QueueId queueId = new QueueId();
		queueId.setName(queueInfo.getName());
		queueId.setQueueId(queueInfo.getQueueId());
		return queueId;
	}
}
