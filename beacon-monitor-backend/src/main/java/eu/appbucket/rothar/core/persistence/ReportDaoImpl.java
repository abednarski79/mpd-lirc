package eu.appbucket.rothar.core.persistence;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import eu.appbucket.rothar.core.domain.report.ReportData;

@Repository
public class ReportDaoImpl implements ReportDao {
	
	private JdbcTemplate jdbcTempalte;
	
	private final static String SQL_INSERT_REPORT_DATA = 
			"INSERT INTO reports(`asset_id`, `latitude`, `longitude`, `created`) "
			+ "VALUES (?, ?, ?, ?, ?)";
	
	@Autowired
	public void setJdbcTempalte(JdbcTemplate jdbcTempalte) {
		this.jdbcTempalte = jdbcTempalte;
	}

	public void createNewEntry(ReportData reportData) {
		jdbcTempalte.update(SQL_INSERT_REPORT_DATA, 
				reportData.getAssetId(),
				reportData.getLatitude(),
				reportData.getLongitude(),
				reportData.getCreated());
	}
}
