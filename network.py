import config
import tensorflow as tf
class NNmodel(tf.keras.Model):#for DQN
	def __init__(self, config:config.config):
		super().__init__()
		self.config = config
		self.hidden_layers = [tf.keras.layers.Dense(size, activation='relu') for size in config.hidden_layers]
		self.output_layer = tf.keras.layers.Dense(config.output_size, activation = 'tanh')
		self.build(config.input_shape)
	
	def call(self, input, training = False):
		x = input
		for layer in self.hidden_layers:
			x = layer(x)
		return self.output_layer(x)