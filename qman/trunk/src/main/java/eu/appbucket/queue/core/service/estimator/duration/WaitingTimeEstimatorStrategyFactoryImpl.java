package eu.appbucket.queue.core.service.estimator.duration;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import eu.appbucket.queue.core.domain.queue.QueueStats;

@Component
public class WaitingTimeEstimatorStrategyFactoryImpl implements WaitingTimeEstimatorStrategyFactory {

	private WaitingTimeEsimationStrategy calculatedWaitingTimeEsimationStraregy;
	private WaitingTimeEsimationStrategy defaultWaitingTimeEsimationStraregy;
	
	@Autowired
	public void setCalculatedWaitingTimeEsimationStrategy(
			CalculatedWaitingTimeEsimationStrategyImpl calculatedWaitingTimeEsimationStraregy) {
		this.calculatedWaitingTimeEsimationStraregy = calculatedWaitingTimeEsimationStraregy;
	}

	@Autowired
	public void setDefaultWaitingTimeEsimationStrategy(
			DefaultWaitingTimeEsimationStrategyImpl defaultWaitingTimeEsimationStraregy) {
		this.defaultWaitingTimeEsimationStraregy = defaultWaitingTimeEsimationStraregy;
	}

	public WaitingTimeEsimationStrategy getStrategy(QueueStats queueStats) {
		if(queueStats.getCalculatedAverageWaitingDuration() != null) {
			return calculatedWaitingTimeEsimationStraregy;
		}		
		return defaultWaitingTimeEsimationStraregy;
	}

	
}
