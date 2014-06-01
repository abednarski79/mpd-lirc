package eu.appbucket.queue.core.persistence;


import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Collection;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;
import org.springframework.stereotype.Repository;

import com.googlecode.ehcache.annotations.Cacheable;
import com.googlecode.ehcache.annotations.TriggersRemove;
import com.googlecode.ehcache.annotations.When;

import eu.appbucket.queue.core.domain.queue.Address;
import eu.appbucket.queue.core.domain.queue.GeographicalLocation;
import eu.appbucket.queue.core.domain.queue.OpeningHours;
import eu.appbucket.queue.core.domain.queue.Openings;
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
	private final static String SQL_SELECT_QUEUE_OPENING_HOURS_BY_QUEUE_ID = "SELECT * FROM queues_opening_hours WHERE queue_id = ?";
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
	
	@Cacheable(cacheName = "queuesCache")
	public Collection<QueueInfo> getQeueues() {		
		List<QueueInfo> queues = jdbcTempalte.query(SQL_SELECT_QUEUES, new QueueInfoMapper());
		return queues;
	}

	@Cacheable(cacheName = "queueInfoCache")
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

	@Cacheable(cacheName = "queueDetailsCache")
	public QueueDetails getQueueDetailsById(int queueId) {
		QueueDetails queueDetails = jdbcTempalte.queryForObject(SQL_SELECT_QUEUE_DETAILS_BY_QUEUE_ID, 
				new QueueDetailsMapper(), queueId);
		queueDetails.setOpenings(getOpeningsById(queueId));
		return queueDetails;
	}
	
	private static final class QueueDetailsMapper implements RowMapper<QueueDetails> {
		public QueueDetails mapRow(ResultSet rs, int rowNum) throws SQLException {
			QueueDetails queueDetails = new QueueDetails();
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
			queueDetails.setDescription((rs.getString("description")));
			queueDetails.setDefaultAverageWaitingDuration(rs.getInt("default_average_waiting_time"));
			return queueDetails;
		}		
	}
	
	private Map<Integer, Openings> getOpeningsById(int queueId) {
		Map<Integer, Openings> dayIdToOpening = new HashMap<Integer, Openings>();
		List<Openings> openings = jdbcTempalte.query(SQL_SELECT_QUEUE_OPENING_HOURS_BY_QUEUE_ID, 
				new OpeningsMapper(), queueId);
		for(Openings opening: openings) {
			dayIdToOpening.put(opening.getDayId(), opening);
		}
		return dayIdToOpening;
	}
	
	public static final class OpeningsMapper implements RowMapper<Openings> {
		
		public Openings mapRow(ResultSet rs, int rowNum) throws SQLException {
			Openings openings = new Openings();
			openings.setDayId(rs.getInt("day_id"));
			OpeningHours openingHoursLocalTimeZone = new OpeningHours();			
			openingHoursLocalTimeZone.setOpeningHour(rs.getInt("opening_hour_local_timezone"));
			openingHoursLocalTimeZone.setOpeningMinute(rs.getInt("opening_minute_local_timezone"));
			openingHoursLocalTimeZone.setClosingHour(rs.getInt("closing_hour_local_timezone"));
			openingHoursLocalTimeZone.setClosingMinute(rs.getInt("closing_minute_local_timezone"));
			openings.setOpeningHoursLocalTimeZone(openingHoursLocalTimeZone);
			OpeningHours openingHoursUTC = new OpeningHours();
			openingHoursUTC.setOpeningHour(rs.getInt("opening_hour_utc"));
			openingHoursUTC.setOpeningMinute(rs.getInt("opening_minute_utc"));
			openingHoursUTC.setClosingHour(rs.getInt("closing_hour_utc"));
			openingHoursUTC.setClosingMinute(rs.getInt("closing_minute_utc"));			
			openings.setOpeningHoursUTC(openingHoursUTC);
			/*OpeningTimes openingTimesUTC = calculateOpeningTimeUTC(openings.getOpeningHoursUTC());*/
			/*openings.setOpeningTimesUTC(openingTimesUTC);*/	
			return openings;
		}	
		
		/*public OpeningTimes calculateOpeningTimeUTC(OpeningHours openingHours) {
			OpeningTimes openingTime = new OpeningTimes();
			Calendar calendar = Calendar.getInstance();
			calendar.setTime(new Date());		
			calendar.set(Calendar.HOUR_OF_DAY, openingHours.getOpeningHour());
			calendar.set(Calendar.MINUTE, openingHours.getOpeningMinute());			
			calendar.set(Calendar.SECOND, 0);
			calendar.set(Calendar.MILLISECOND, 0);
			openingTime.setOpeningTime(calendar.getTimeInMillis());
			calendar.setTime(new Date());
			calendar.set(Calendar.HOUR_OF_DAY, openingHours.getClosingHour());
			calendar.set(Calendar.MINUTE, openingHours.getClosingMinute());
			calendar.set(Calendar.SECOND, 0);
			calendar.set(Calendar.MILLISECOND, 0);
			openingTime.setClosingTime(calendar.getTimeInMillis());			
			return openingTime;
		}*/
	}
	
	@TriggersRemove(cacheName = "queueStatsCache", when = When.AFTER_METHOD_INVOCATION, removeAll = true)
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
	
	@Cacheable(cacheName = "queueStatsCache")
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