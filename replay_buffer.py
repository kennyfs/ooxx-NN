import os
import random
from abc import ABC, abstractmethod

import numpy as np

import config
import tensorflow as tf

class Trajectory:
	def __init__(self):
		self.obseravations = []
		self.actions = []
		self.length = 0
		self.result = None

	def add(self, state, action):
		self.obseravations.append(state)
		self.actions.append(action)
		self.length += 1
	
	def make_target(self, state_index:int):
		if self.result == None:
			return 0
		if state_index%2 == self.result:
			return 1
		else:
			return -1

class AbstractDataContainer(ABC):
	def __init__(self, config:config.config):
		super().__init__()
		pass

	@abstractmethod
	def save_game(self, T:Trajectory):
		pass

	@abstractmethod
	def get_data(self):#only replay buffer requires batch_size
		pass

class DataContainer:
	def __new__(cls, config:config.config):
		if config.datacontainer == "ReplayBuffer":
			return ReplayBuffer(config)
		elif config.datacontainer == "AllData":
			return AllData(config)
		else:
			raise NotImplementedError
			
class ReplayBuffer(AbstractDataContainer):
	def __init__(self, config:config.config):
		self.buffer = {}
		self.num_played_games = 0
		self.num_played_games = 0
		self.total_samples = 0
		self.rotate = config.rotate
		self.flip = config.flip

	def save_game(self, T:Trajectory):
		self.buffer[self.num_played_games] = T
		self.num_played_games += 1
		self.num_played_steps += T.length
		self.total_samples += T.length

		if self.config.replay_buffer_size < len(self.buffer):
			del_id = self.num_played_games - len(self.buffer)
			self.total_samples -= self.buffer[del_id].length
			del self.buffer[del_id]

		if self.config.save_game_to_file:
			T.save(os.path.join(self.config.save_game_dir, f'{self.num_played_games}.record'))
	
	def get_data(self, batch_size):
		#samples always start from state followed by actions of type 0 (move)
		#return type: np.array
		(
			observation_batch,
			action_batch,
			value_batch,
		) = ([], [], [])

		for game_id, T in self.sample_n_games(batch_size):
			game_pos = self.sample_position(T)

			observation = T.observations[game_pos]
			action = T.actions[game_pos]
			value = T.make_target(game_pos)
			if action > 8:
				action -= 9
				#swap action
				observation = tf.reverse(observation, axis = 0)

			if self.rotate:
				dict = {0:6, 1:3, 2:0, 3:7, 4:4, 5:1, 6:8, 7:5, 8:2}
				for rotate in range(4):
					new_observation = np.rot90(observation, rotate, (1, 2))
					new_action = action
					for _ in rotate:
						new_action = dict[new_action]
					observation_batch.append(new_observation)
					action_batch.append(new_action)

					if self.flip:
						new_observation = np.flip(new_observation, 1)
						dict = {0:6, 1:7, 2:8, 3:3, 4:4, 5:5, 6:0, 7:1, 8:2}
						new_action = dict[new_action]
						observation_batch.append(new_observation)
						action_batch.append(new_action)

			
			for _ in range((4 if self.rotate else 1)*(2 if self.flip else 1)):
				value_batch.append(value)

		# observation_batch: batch, channels, height, width
		# action_batch: batch, 1
		# value_batch: batch, 1
		return (
				np.array(observation_batch, dtype = np.float32),
				np.array(action_batch, dtype = np.int32),
				np.array(value_batch, dtype = np.float32),
		)

	def sample_n_games(self, n_games, force_uniform = True):
		if force_uniform:
			selected_games = np.random.choice(list(self.buffer.keys()), n_games)
		else:
			raise NotImplementedError
		ret = [(game_id, self.buffer[game_id])
			   for game_id in selected_games]
		return ret
	
	def sample_position(self, T:Trajectory, force_uniform = True):
		if force_uniform:
			return np.random.choice(T.length)
		else:
			raise NotImplementedError

class AllData(AbstractDataContainer):
	def __init__(self, config:config.config):
		self.observation_batch = []
		self.action_batch = []
		self.value_batch = []

	def save_game(self, T:Trajectory):
		for game_pos in range(T.length):

			observation = T.observations[game_pos]
			action = T.actions[game_pos]
			value = T.make_target(game_pos)
			if action > 8:
				action -= 9
				#swap action
				observation = tf.reverse(observation, axis = 0)
			
			dict = {0:6, 1:3, 2:0, 3:7, 4:4, 5:1, 6:8, 7:5, 8:2}
			for rotate in range(4):
				new_observation = np.rot90(observation, rotate, (1, 2))
				new_action = action
				for _ in rotate:
					new_action = dict[new_action]
				self.observation_batch.append(new_observation)
				self.action_batch.append(new_action)

				#flip again
				new_observation = np.flip(new_observation, 1)
				dict = {0:6, 1:7, 2:8, 3:3, 4:4, 5:5, 6:0, 7:1, 8:2}
				new_action = dict[new_action]
				self.observation_batch.append(new_observation)
				self.action_batch.append(new_action)
			
			for _ in range(8):
				self.value_batch.append(value)
	def get_data(self):
		return self.observation_batch, self.action_batch, self.value_batch
