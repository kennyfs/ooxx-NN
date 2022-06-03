import agent
import config
import network
import replay_buffer
import self_play
import tensorflow as tf

class Main:
	def __init__(self):
		self.config = config.default_config()
	
	def selfplay_and_train(self):
		self.model = network.NNmodel(self.config)
		self.DQNagent = agent.DQNagent(self.config, self.model)
		self.data = replay_buffer.DataContainer(self.config)

		self.selfplay = self_play.SelfPlay(self.config)
		self.selfplay.play_games(self.DQNagent, self.data)

		observation, action, value = self.data.get_data()
		observation = tf.reshape(observation, [observation.shape[0], -1])
		action = tf.one_hot(action, 9)
		input = tf.concat([observation, action], axis = 1)
		self.model.fit(input, value, batch_size = 1024, epochs = 50)
if __name__ == "__main__":
	'''oplist = [
		"load data",
		"selfplay and train",
		"train from data",
		"display game",
	]
	print("Choose from the following options:")
	for i, op in enumerate(oplist):
		print(f"{i+1}: {op}")
	op = int(input())
	while op not in range(len(oplist)):
		print("Invalid input")
		for i, op in enumerate(oplist):
			print(f"{i+1}: {op}")
		op = int(input())'''
	op = 2
	main = Main()
	if op == 1:
		pass
	elif op == 2:
		main.selfplay_and_train()
	elif op == 3:
		pass
	elif op == 4:
		pass
	else:
		raise NotImplementedError
