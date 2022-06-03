from abc import ABC, abstractmethod

import numpy as np
import tensorflow as tf

import config
import network


class AbstractAgent(ABC):
	def __init__(self):
		super().__init__()
		pass
	
	@abstractmethod
	def act(self, state, color):
		pass

class DQNagent(AbstractAgent):
	def __init__(self, config:config.config, model:network.NNmodel):
		self.config = config
		self.model = model
	
	def act(self, state, color):
		one_hot_action = tf.concat([tf.expand_dims(tf.one_hot(i, 9), 0) for i in range(9)], axis = 0)
		value = tf.squeeze(self.model(tf.concat([tf.tile(tf.reshape(state, (1, -1)), [9, 1]), one_hot_action], axis = 1)))
		value /= self.config.temperature
		value = tf.nn.softmax(value).numpy()
		value /= np.sum(value)
		return np.random.choice(9, p = value) + color * 9
