import tensorflow as tf

'''
action:
0~8 1
9~17 2
'''
class Env:
	result_matric=tf.constant([[[1,1,1],[0,0,0],[0,0,0]],[[0,0,0],[1,1,1],[0,0,0]],[[0,0,0],[0,0,0],[1,1,1]],[[1,0,0],[1,0,0],[1,0,0]],[[0,1,0],[0,1,0],[0,1,0]],[[0,0,1],[0,0,1],[0,0,1]],[[1,0,0],[0,1,0],[0,0,1]],[[0,0,1],[0,1,0],[1,0,0]]], dtype = tf.float32)
	def __init__(self):
		self.reset()

	def reset(self):
		self.grid = tf.zeros((2,3,3), dtype=tf.float32)

	def step(self, action):
		color = action//9
		action -= color*9
		x = action//3
		y = action%3
		if self.grid[color, x, y] == 1.0:
			return -1.0
		self.grid[color, x, y] = 1.0
		res = self.result()
		if res != None:
			return 1.0
		return 0.0
	
	def render(self):
		for i in range(3):
			for j in range(3):
				if self.grid[0, i, j] == 1.0:
					print('O', end = '')
				elif self.grid[1, i, j] == 1.0:
					print('X', end = '')
				else:
					print('.', end = '')
				if self.grid[0, i, j] == 1.0 and self.grid[1, i, j] == 1.0:
					raise ValueError(f'grid[{i}][{j}] is both O and X')
			print()
	
	def result(self):
		res = None
		for color in range(2):
			for matric in self.result_matric:
				if tf.math.reduce_all(tf.math.equal(tf.math.multiply(self.grid[color], matric), matric)):
					if res != None and res != color:
						self.render()
						raise ValueError(f'grid is not a valid result')
					res = color
		return res
	
	def terminate(self):
		return self.result() != None

	def get_state(self):
		return self.grid
