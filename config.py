class config:
	def __init__(self,
		hidden_layers,
	):
		self.hidden_layers = hidden_layers
		self.output_size = 1
		self.input_shape = (None, 27)
		self.game_count_per_iteration = 5
		self.training_steps_to_selfplay_steps_ratio = 2.0
		self.num_selfplay_game_per_iteration = 1
		self.datacontainer = 'AllData'
		self.optimizer = "Adam"
		self.loss = "MSE"
		self.temperature = 0.5
def default_config():
	return config(
		hidden_layers=[64]*3,
	)
