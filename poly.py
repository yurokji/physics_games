RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

import math
import pygame
from pygame import rect

class Polygon:
	# (_mass: 질량, _s0: 초기 위치, _v0: 초기 속도, _acc: 물체의 가속도)
	# 화면에 공을 표시할 속성(_radius: 반지름, , _color) 넣어
	# 객체를 초기화시켜주세요
	def __init__(self,
		mass=1, points=[(50,200), (30, 220), (330, 520), (350, 500)], v0=[0, 0], a=[0, 0], size=[10,10], mu_k=0, color=WHITE):
		self.g = [0, 9.8]	
		self.a = [self.g[0], self.g[1]]
		self.mass = mass
		self.size = size
		self.t = 0
		self.points = points
		self.s0 = points[0]
		self.s = [self.s0[0], self.s0[1]]
		self.v0 = v0
		self.v = [self.v0[0], self.v0[1]]
		self.mu_k = mu_k
		self.color = color


	# 물체에 중력 이외의 힘을 가한다
	def applyForce(self, force):
		self.a[0] += force[0] / self.mass 
		self.a[1] += force[1] / self.mass 

	def computePos(self, delta_t=0.01):
		self.v[0] = self.v0[0] + self.a[0] * delta_t
		self.v[1] = self.v0[1] + self.a[1] * delta_t
		self.s[0] = self.s0[0] + (self.v[0] * delta_t)
		self.s[1] = self.s0[1] + (self.v[1] * delta_t)
		self.v0[0] = self.v[0]
		self.v0[1] = self.v[1]
		self.s0[0] = self.s[0]
		self.s0[1] = self.s[1]
		self.t += delta_t
	

	def collide(self, other):
		myRect = self.getRect()
		otherRect = other.getRect()
		if myRect.left < otherRect.right and myRect.right > otherRect.left:
			if myRect.top < otherRect.bottom and myRect.bottom > otherRect.top:
				return True
		return False

	# def getRect(self):
	# 	return Rect(self.s[0], self.s[1], self.size[0], self.size[1])
