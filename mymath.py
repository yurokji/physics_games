import math

class Vec2:
	def __init__(self, input_list):
		self.x = input_list[0]
		self.y = input_list[1]

	def length(self):
		return math.sqrt(self.x * self.x + self.y  * self.y)

	def normalize(self):
		x = self.x / self.length()
		y = self.y / self.length()
		return Vec2([x,y])

	def dot(self, v, power=1):
		return self.x * v.x + self.y * v.y

	def toList(self):
		return [self.x, self.y]

	def __add__(self, v):
		if isinstance(v, Vec2):
			return Vec2([self.x + v.x, self.y + v.y])
		elif isinstance(v, int) or isinstance(v, float):
			return Vec2([self.x + v, self.y + v])
		else:
			raise Exception(v, "is not supported in Vec2")

	def __sub__(self, v):
		if isinstance(v, Vec2):
			return Vec2([self.x - v.x, self.y - v.y])
		elif isinstance(v, int) or isinstance(v, float):
			return Vec2([self.x - v, self.y - v])
		else:
			raise Exception(v, "is not supported in Vec2")
	
	def __mul__(self, v):
		if isinstance(v, Vec2):
			return Vec2([self.x * v.x, self.y * v.y])
		elif isinstance(v, int) or isinstance(v, float):
			return Vec2([self.x * v, self.y * v])
		else:
			raise Exception(v, "is not supported in Vec2")


	def __truediv__(self, v):
		if isinstance(v, Vec2):
			return Vec2([self.x / v.x, self.y / v.y])
		elif isinstance(v, int) or isinstance(v, float):
			return Vec2([self.x / v, self.y / v])
		else:
			raise Exception(v, "is not supported in Vec2")

	def __itruediv__(self, v):
		if isinstance(v, Vec2):
			return Vec2([self.x / v.x, self.y / v.y])
		elif isinstance(v, int) or isinstance(v, float):
			return Vec2([self.x / v, self.y / v])
		else:
			raise Exception(v, "is not supported in Vec2")



