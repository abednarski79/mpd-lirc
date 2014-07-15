package eu.appbucket.rothar.web.domain.report;

import java.util.Date;

import eu.appbucket.rothar.core.domain.report.ReportData;

public class ReportEntry {

	private String assetId;
	private double latitude;
	private double longitude;
	private Date created;
	private String url;

	public String getAssetId() {
		return assetId;
	}

	public void setAssetId(String assetId) {
		this.assetId = assetId;
	}

	public double getLatitude() {
		return latitude;
	}

	public void setLatitude(double latitude) {
		this.latitude = latitude;
	}

	public double getLongitude() {
		return longitude;
	}

	public void setLongitude(double longitude) {
		this.longitude = longitude;
	}

	public Date getCreated() {
		return created;
	}

	public void setCreated(Date created) {
		this.created = created;
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}
	
	public static ReportEntry fromReportData(ReportData data) {
		ReportEntry entry = new ReportEntry();
		entry.setAssetId(data.getAssetId());
		entry.setLongitude(entry.getLongitude());
		entry.setLatitude(data.getLatitude());
		entry.setCreated(data.getCreated());
		return entry;
	}
}
