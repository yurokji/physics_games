RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Ball:
	def __init__(self, 
		_size=10, 
		_color=WHITE, 
		_mass=1, 
		_init_pos=[100, 500], 
		_init_speed=[0,0], 
		_accel=[3,0]):

		self.color = _color
		self.mass = _mass
		self.size = 10 * self.mass
		self.s0 = _init_pos
		self.s = [self.s0[0], self.s0[1]]
		self.v0 = _init_speed
		self.v = [self.v0[0], self.v0[1]]
		self.g = [0, 9.8]
		self.time = 0
		self.accel = _accel

	def setAccel(self, _accel):
		self.accel = _accel


	def setPos(self, _time=0.01):
		self.time += _time
		accel = [0,0]
		accel[0] = self.accel[0] + self.g[0]
		accel[1] = self.accel[1] + self.g[1]
		self.accel[1] + self.g[1]
		self.v[0] = self.v0[0] + accel[0] * _time
		self.v[1] = self.v0[1] + accel[1] * _time
		self.s[0] = self.s0[0] +  (self.v0[0] * _time) + (0.5 * accel[0] * _time * _time)
		self.s[1] = self.s0[1] +  (self.v0[1] * _time) + (0.5 * accel[1] * _time * _time)
		self.v0[0] = self.v[0]
		self.v0[1] = self.v[1]
		self.s0[0] = self.s[0]
		self.s0[1] = self.s[1]
		print(self.s)



