class config:
	def __init__(self,
		hidden_layers,
	):
		self.hidden_layers = hidden_layers
		self.output_size = 1
		self.input_shape = (None, 36)
def default_config():
	return config(
		hidden_layers=[64]*3,
	)