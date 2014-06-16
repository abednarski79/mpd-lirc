package eu.appbucket.queue.core.persistence;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Collection;
import java.util.Date;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import eu.appbucket.queue.core.domain.queue.QueueInfo;
import eu.appbucket.queue.core.domain.ticket.TicketUpdate;

@Repository
public class TicketDaoImpl implements TicketDao {
	
	private final static String SQL_INSERT_TICKET_UPDATE = 
			"INSERT INTO updates(`queue_id`, `user_ticket`, `served_ticket`, `created`, `quality`) "
			+ "VALUES (?, ?, ?, ?, ?)";
	
	private final static String SQL_SELECT_TICKET_UPDATES_BY_QUEUE_AND_TIMESTAMP = 
			"SELECT * FROM updates WHERE queue_id = ? AND created >= ? AND created <= ? AND quality >= ?";
	
	private final static String SQL_SELECT_TICKET_UPDATE_WITH_HIGHEST_TICKET_NUMBER_BY_QUEUE_AND_TIMESTAMP = 
			"SELECT * FROM updates WHERE queue_id = ? AND created >= ? AND created <= ? AND quality >= ? order by served_ticket desc LIMIT 1";
	
	private JdbcTemplate jdbcTempalte;
	
	@Autowired
	public void setJdbcTempalte(JdbcTemplate jdbcTempalte) {
		this.jdbcTempalte = jdbcTempalte;
	}
	
	@CacheEvict(value = "highestTicketUpdateCache", key="#queueId")
	public void storeTicketUpdate(TicketUpdate ticketUpdate) {		
		jdbcTempalte.update(SQL_INSERT_TICKET_UPDATE, 
				ticketUpdate.getQueueInfo().getQueueId(),
				ticketUpdate.getClientTicketNumber(),
				ticketUpdate.getCurrentlyServicedTicketNumber(),
				ticketUpdate.getCreated(),
				ticketUpdate.getQuality());
	}
	
	@CacheEvict(value = "highestTicketUpdateCache", key="#queueInfo.queueId")
	public void cleanHighestTicketUpdateByQueueAndDayCache(QueueInfo queueInfo) {
	}
	
	public Collection<TicketUpdate> readTicketUpdatesByQueueAndDate(
			QueueInfo queueInfo, Date fromDate, Date toDate, int minAcceptedInputQuality) {		
		Collection<TicketUpdate> ticketUpdates = jdbcTempalte.query(
				SQL_SELECT_TICKET_UPDATES_BY_QUEUE_AND_TIMESTAMP, 
				new TicketUpdateMapper(),
				queueInfo.getQueueId(), 
				fromDate, toDate,
				minAcceptedInputQuality);
		return ticketUpdates;
	}

	private static final class TicketUpdateMapper implements RowMapper<TicketUpdate> {
		public TicketUpdate mapRow(ResultSet rs, int rowNum) throws SQLException {
			TicketUpdate ticketUpdate = new TicketUpdate();
			QueueInfo queueInfo = new QueueInfo();
			queueInfo.setQueueId(rs.getInt("queue_id"));
			ticketUpdate.setQueueInfo(queueInfo);
			ticketUpdate.setClientTicketNumber(rs.getInt("user_ticket"));
			ticketUpdate.setCurrentlyServicedTicketNumber(rs.getInt("served_ticket"));
			ticketUpdate.setCreated(rs.getTimestamp("created"));
			ticketUpdate.setQuality(rs.getInt("quality"));
			return ticketUpdate;
		}		
	}
	
	@Cacheable(value = "highestTicketUpdateCache" , key = "#queueInfo.queueId")
	public TicketUpdate readHighestTicketUpdateByQueueAndDay(
			QueueInfo queueInfo, Date fromDate, Date toDate, int minAcceptedInputQuality) {
		TicketUpdate highestTicketUpdate = null;
		try {
			highestTicketUpdate = jdbcTempalte.queryForObject(
					SQL_SELECT_TICKET_UPDATE_WITH_HIGHEST_TICKET_NUMBER_BY_QUEUE_AND_TIMESTAMP,
					new TicketUpdateMapper(),
					queueInfo.getQueueId(), 
					fromDate, toDate,
					minAcceptedInputQuality);
		} catch (EmptyResultDataAccessException e) {
			highestTicketUpdate = new TicketUpdate();
		}
		return highestTicketUpdate;
	}
}
