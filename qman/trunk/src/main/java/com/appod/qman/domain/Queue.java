package com.appod.qman.domain;

public class Queue {
	
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
	public String toString() {
		return "Queue [queueId=" + queueId + ", name=" + name + "]";
	}
}
