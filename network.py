import tensorflow as tf

import config
import replay_buffer


class NNmodel(tf.keras.Model):#for DQN
	def __init__(self, config:config.config):
		super().__init__()
		self.config = config
		self.hidden_layers = [tf.keras.layers.Dense(size, activation='relu') for size in config.hidden_layers]
		self.output_layer = tf.keras.layers.Dense(config.output_size, activation = 'tanh')
		self.build(config.input_shape)
		
		self.compile(
			optimizer = self.config.optimizer,
			loss = self.config.loss,
		)
	def call(self, input, training = False):
		x = input
		for layer in self.hidden_layers:
			x = layer(x)
		return self.output_layer(x)

	def train_step(self, data):
		x, y = data

		with tf.GradientTape() as tape:
			y_pred = self(x, training=True)  # Forward pass
			# Compute the loss value
			# (the loss function is configured in `compile()`)
			loss = self.compiled_loss(y, y_pred, regularization_losses=self.losses)

		# Compute gradients
		trainable_vars = self.trainable_variables
		gradients = tape.gradient(loss, trainable_vars)
		# Update weights
		self.optimizer.apply_gradients(zip(gradients, trainable_vars))
		# Update metrics (includes the metric that tracks the loss)
		self.compiled_metrics.update_state(y, y_pred)
		# Return a dict mapping metric names to current value
		return {m.name: m.result() for m in self.metrics}