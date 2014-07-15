package eu.appbucket.rothar.core.persistence;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import eu.appbucket.rothar.core.domain.report.ReportData;

@Repository
public class ReportDaoImpl implements ReportDao {
	
	private JdbcTemplate jdbcTempalte;
	
	private final static String SQL_INSERT_REPORT_DATA = 
			"INSERT INTO reports(`asset_id`, `latitude`, `longitude`, `created`) "
			+ "VALUES (?, ?, ?, ?)";
	
	private final static String SQL_SELECT_REPORT_DATA = 
			"SELECT * FROM reports";
	
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

	public List<ReportData> getAllReportEntries() {
		List<ReportData> reports = jdbcTempalte.query(SQL_SELECT_REPORT_DATA, new ReportMapper());
		return reports;
	}
	
	private static final class ReportMapper implements RowMapper<ReportData> {
		public ReportData mapRow(ResultSet rs, int rowNum) throws SQLException {
			ReportData report = new ReportData();
			report.setAssetId(rs.getString("asset_id"));
			report.setLongitude(rs.getDouble("longitude"));
			report.setLatitude(rs.getDouble("latitude"));
			report.setCreated(rs.getDate("created"));
			return report;
		}
	} 
}
