package com.appod.qman.persistence;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Collection;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;
import org.springframework.stereotype.Repository;

import com.appod.qman.domain.Queue;

@Repository
public class QueueDaoImpl implements QueueDao {

	private SimpleJdbcTemplate jdbcTempalte;
	
	private final static String SQL_SELECT_QUEUES = "SELECT queue_id, name FROM queues";
	private final static String SQL_SELECT_QUEUE_BY_ID = "SELECT queue_id, name FROM queues WHERE queue_id = ?";
		
	public Collection<Queue> getQeueues() {		
		List<Queue> queues = jdbcTempalte.query(SQL_SELECT_QUEUES, new QueueMapper());
		return queues;
	}

	public Queue getQueueById(int queueId) {		
		return jdbcTempalte.queryForObject(SQL_SELECT_QUEUE_BY_ID, new QueueMapper(), queueId);
	}
	
	private static final class QueueMapper implements RowMapper<Queue> {
		public Queue mapRow(ResultSet rs, int rowNum) throws SQLException {
			Queue queue = new Queue();
			queue.setQueueId(rs.getInt(1));
			queue.setName(rs.getString(2));
			return queue;
		}
		
	} 
	
	@Autowired
	public void setJdbcTempalte(SimpleJdbcTemplate jdbcTempalte) {
		this.jdbcTempalte = jdbcTempalte;
	}
}
