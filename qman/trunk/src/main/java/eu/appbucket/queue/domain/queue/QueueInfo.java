package eu.appbucket.queue.domain.queue;

public class QueueInfo {
	
	private int queueId;
	private String name;
	private String imageUrl;

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
	
	public String getImageUrl() {
		return imageUrl;
	}

	public void setImageUrl(String imageUrl) {
		this.imageUrl = imageUrl;
	}

	@Override
	public String toString() {
		return "QueueInfo [queueId=" + queueId + ", name=" + name
				+ ", imageUrl=" + imageUrl + "]";
	}
}
