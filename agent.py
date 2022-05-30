import environment
import config
import network
import tensorflow as tf
import numpy as np
class DQNagent:
	def __init__(self, config:config.config):
		self.config = config
		self.model = network.NNmodel(config)
	
	def act(self, state, color):
		value = [self.model(tf.concat([state, tf.one_hot(action + color * 9, 18)], axis = 0)) for action in range(9)]
		value /= self.config.temperature
		value = tf.nn.softmax(value)
		return np.random.choice(9, p = value) + color*9
	
	def selfplay(self):
		for i in range(self.config.game_count):
			t = 0
			rewards = 0
			env = environment.Env()
			while not env.terminate():
				action = self.act(env.get_state(), t%2)
				rewards += env.step(action)
				env.render()
				t += 1