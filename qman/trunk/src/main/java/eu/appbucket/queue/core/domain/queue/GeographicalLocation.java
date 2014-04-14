package eu.appbucket.queue.core.domain.queue;

public class GeographicalLocation {

	private float latitude;
	private float longitude;

	public float getLatitude() {
		return latitude;
	}

	public void setLatitude(float latitude) {
		this.latitude = latitude;
	}

	public float getLongitude() {
		return longitude;
	}

	public void setLongitude(float longitude) {
		this.longitude = longitude;
	}

	@Override
	public String toString() {
		return "GeographicalLocation [latitude=" + latitude + ", longitude="
				+ longitude + "]";
	}
}
