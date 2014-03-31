package eu.appbucket.queue.persistence;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Calendar;
import java.util.Collection;
import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;
import org.springframework.stereotype.Repository;

import eu.appbucket.queue.domain.queue.Address;
import eu.appbucket.queue.domain.queue.GeographicalLocation;
import eu.appbucket.queue.domain.queue.OpeningHours;
import eu.appbucket.queue.domain.queue.OpeningTimes;
import eu.appbucket.queue.domain.queue.QueueDetails;
import eu.appbucket.queue.domain.queue.QueueInfo;

@Repository
public class QueueDaoImpl implements QueueDao {

	private SimpleJdbcTemplate jdbcTempalte;
	
	private final static String SQL_SELECT_QUEUES = "SELECT * FROM queues";
	private final static String SQL_SELECT_QUEUE_INFO_BY_ID = "SELECT * FROM queues WHERE queue_id = ?";
	private final static String SQL_SELECT_QUEUE_DETAILS_BY_ID = "SELECT * FROM queues_details WHERE queue_id = ?";
		
	@Autowired
	public void setJdbcTempalte(SimpleJdbcTemplate jdbcTempalte) {
		this.jdbcTempalte = jdbcTempalte;
	}
	
	public Collection<QueueInfo> getQeueues() {		
		List<QueueInfo> queues = jdbcTempalte.query(SQL_SELECT_QUEUES, new QueueInfoMapper());
		return queues;
	}

	public QueueInfo getQueueInfoById(int queueId) {		
		return jdbcTempalte.queryForObject(SQL_SELECT_QUEUE_INFO_BY_ID, new QueueInfoMapper(), queueId);
	}
	
	private static final class QueueInfoMapper implements RowMapper<QueueInfo> {
		public QueueInfo mapRow(ResultSet rs, int rowNum) throws SQLException {
			QueueInfo queue = new QueueInfo();
			queue.setQueueId(rs.getInt("queue_id"));
			queue.setName(rs.getString("name"));
			return queue;
		}
		
	} 

	public QueueDetails getQueueDetailsById(int queueId) {
		return jdbcTempalte.queryForObject(SQL_SELECT_QUEUE_DETAILS_BY_ID, new QueueDetailsMapper(), queueId);
	}
	
	private static final class QueueDetailsMapper implements RowMapper<QueueDetails> {
		public QueueDetails mapRow(ResultSet rs, int rowNum) throws SQLException {
			QueueDetails queueDetails = new QueueDetails();
			OpeningHours openingHour = new OpeningHours();
			openingHour.setOpeningHour(rs.getInt("opening_hour"));
			openingHour.setOpeningMinute(rs.getInt("opening_minute"));
			openingHour.setClosingHour(rs.getInt("closing_hour"));
			openingHour.setClosingMinute(rs.getInt("closing_minute"));
			queueDetails.setOpeningHours(openingHour);		
			GeographicalLocation location = new GeographicalLocation();
			location.setLatitude(rs.getFloat("latitude"));
			location.setLongitude(rs.getFloat("longitude"));			
			queueDetails.setLocation(location);
			Address address = new Address();
			address.setAddressLine1(rs.getString("address_line_1"));
			address.setAddressLine2(rs.getString("address_line_2"));
			address.setCountry(rs.getString("country"));
			address.setCounty(rs.getString("county"));
			address.setPostcode(rs.getString("post_code"));
			address.setTownOrCity(rs.getString("town_city"));
			queueDetails.setAddress(address);
			queueDetails.setEmail((rs.getString("email")));
			queueDetails.setPhoneNumber((rs.getString("phone_number")));
			return queueDetails;
		}		
	} 
}
