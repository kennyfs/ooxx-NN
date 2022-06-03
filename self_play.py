import numpy as np
import tensorflow as tf

import agent
import environment
import replay_buffer
import config

class SelfPlay:
	def __init__(self, config:config.config):
		self.config = config
	def play_games(self, agent:agent.AbstractAgent, buffer:replay_buffer.DataContainer):
		for _ in range(self.config.game_count_per_iteration):
			t = 0
			env = environment.Env()
			T = replay_buffer.Trajectory()
			while not env.terminate():
				state = env.get_state()
				action = agent.act(state, t%2)
				env.step(action)
				env.render()
				T.add(state, action)
				t += 1
			T.result = env.result()
			buffer.save_game(T)
