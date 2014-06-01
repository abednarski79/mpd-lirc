package eu.appbucket.queue.web.domain.office.element;

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

	public static GeographicalLocation fromGeographicalLocation(
			eu.appbucket.queue.core.domain.queue.GeographicalLocation geographicalLocationInput) {
		GeographicalLocation geographicalLocation = new GeographicalLocation();
		geographicalLocation.setLatitude(geographicalLocationInput.getLatitude());
		geographicalLocation.setLongitude(geographicalLocationInput.getLongitude());
		return geographicalLocation;
	}
}
