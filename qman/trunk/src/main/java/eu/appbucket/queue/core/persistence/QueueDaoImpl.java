package eu.appbucket.queue.core.persistence;


import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Collection;
import java.util.Date;
import java.util.List;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;
import org.springframework.stereotype.Repository;

import eu.appbucket.queue.core.domain.queue.Address;
import eu.appbucket.queue.core.domain.queue.GeographicalLocation;
import eu.appbucket.queue.core.domain.queue.OpeningHours;
import eu.appbucket.queue.core.domain.queue.QueueDetails;
import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.queue.QueueStats;

@Repository
public class QueueDaoImpl implements QueueDao {

	private SimpleJdbcTemplate jdbcTempalte;
	private static final Logger LOGGER = Logger.getLogger(QueueDaoImpl.class);
	
	private final static String SQL_SELECT_QUEUES = "SELECT * FROM queues";
	private final static String SQL_SELECT_QUEUE_INFO_BY_QUEUE_ID = "SELECT * FROM queues WHERE queue_id = ?";
	private final static String SQL_SELECT_QUEUE_DETAILS_BY_QUEUE_ID = "SELECT * FROM queues_details WHERE queue_id = ?";
	private final static String SQL_SELECT_CALCULATED_AVERAGE_WAITING_TIME_BY_QUEUE_ID_AND_DATE = 
			"SELECT calculated_average_waiting_time FROM queues_stats WHERE date = ? AND queue_id = ?";
	private final static String SQL_UPDATE_QUEUE_STATS_BY_QUEUE_ID_AND_DATE = 
			"UPDATE queues_stats SET calculated_average_waiting_time = ? WHERE date = ? AND queue_id = ?";
	private final static String SQL_INSERT_QUEUE_STATS_BY_QUEUE_ID_AND_DATE = 
			"INSERT INTO queues_stats (queue_id, date, calculated_average_waiting_time) VALUES (?, ?, ?)";	
	
	@Autowired
	public void setJdbcTempalte(SimpleJdbcTemplate jdbcTempalte) {
		this.jdbcTempalte = jdbcTempalte;
	}
	
	public Collection<QueueInfo> getQeueues() {		
		List<QueueInfo> queues = jdbcTempalte.query(SQL_SELECT_QUEUES, new QueueInfoMapper());
		return queues;
	}

	public QueueInfo getQueueInfoById(int queueId) {		
		return jdbcTempalte.queryForObject(SQL_SELECT_QUEUE_INFO_BY_QUEUE_ID, new QueueInfoMapper(), queueId);
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
		return jdbcTempalte.queryForObject(SQL_SELECT_QUEUE_DETAILS_BY_QUEUE_ID, new QueueDetailsMapper(), queueId);
	}
	
	private static final class QueueDetailsMapper implements RowMapper<QueueDetails> {
		public QueueDetails mapRow(ResultSet rs, int rowNum) throws SQLException {
			QueueDetails queueDetails = new QueueDetails();
			OpeningHours openingHoursLocalTimeZone = new OpeningHours();			
			openingHoursLocalTimeZone.setOpeningHour(rs.getInt("opening_hour_local_timezone"));
			openingHoursLocalTimeZone.setOpeningMinute(rs.getInt("opening_minute_local_timezone"));
			openingHoursLocalTimeZone.setClosingHour(rs.getInt("closing_hour_local_timezone"));
			openingHoursLocalTimeZone.setClosingMinute(rs.getInt("closing_minute_local_timezone"));
			queueDetails.setOpeningHoursLocalTimeZone(openingHoursLocalTimeZone);
			OpeningHours openingHoursUTC = new OpeningHours();
			openingHoursUTC.setOpeningHour(rs.getInt("opening_hour_utc"));
			openingHoursUTC.setOpeningMinute(rs.getInt("opening_minute_utc"));
			openingHoursUTC.setClosingHour(rs.getInt("closing_hour_utc"));
			openingHoursUTC.setClosingMinute(rs.getInt("closing_minute_utc"));			
			queueDetails.setOpeningHoursUTC(openingHoursUTC);
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
			queueDetails.setDefaultAverageWaitingDuration(rs.getInt("default_average_waiting_time"));
			return queueDetails;
		}		
	}

	public void storeQueueStats(QueueStats queueStats) {
		int numberOfUpdatedRows = jdbcTempalte.update(SQL_UPDATE_QUEUE_STATS_BY_QUEUE_ID_AND_DATE,
				queueStats.getCalculatedAverageWaitingDuration(),
				queueStats.getDate(),
				queueStats.getQueueInfo().getQueueId());
		if(numberOfUpdatedRows == 0) {			
			jdbcTempalte.update(SQL_INSERT_QUEUE_STATS_BY_QUEUE_ID_AND_DATE,
					queueStats.getQueueInfo().getQueueId(),
					queueStats.getDate(),
					queueStats.getCalculatedAverageWaitingDuration());			
		}
	}

	public QueueStats getQueueStatsByIdAndDate(int queueId, Date statsDate) {
		QueueStats queueStats = new QueueStats();
		queueStats.setDate(statsDate);
		queueStats.setQueueInfo(this.getQueueInfoById(queueId));
		try {
			queueStats.setCalculatedAverageWaitingDuration(
					jdbcTempalte.queryForInt(SQL_SELECT_CALCULATED_AVERAGE_WAITING_TIME_BY_QUEUE_ID_AND_DATE, statsDate, queueId));				
		} catch (EmptyResultDataAccessException dataAccessException) {
			LOGGER.info("No stats available for queue: " + queueId + " date: " + statsDate);
		}
		return queueStats;
	}
}
