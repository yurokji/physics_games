RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
from aabb import *

import math
class Ball:
	# 물리 시뮬레이션에 필요한 속성들
	# (_mass: 질량, _s0: 초기 위치, _v0: 초기 속도, _acc: 물체의 가속도)
	# 화면에 공을 표시할 속성(_radius: 반지름, , _color) 넣어
	# 객체를 초기화시켜주세요
	def __init__(self,
		mass=1, s0=[0, 0], v0=[0, 0], a=[0, 0], radius=10, color=WHITE):

		# g: 중력 가속도
		# x방향으로는 중력이 작용하지 않으므로 0을 넣어준다 
		# y방향으로는 9.8이 아닌 -9.8을 넣어준다.
		# (화면 좌표 아래방향은 y가 증가하는 방향이므로)
		self.g = [0, 10]	
		# 현재는 물체에 작용하는 힘이 없으므로
		# 최종 가속도 방향은 중력 방향뿐이다.
		self.a = [self.g[0], self.g[1]]
		# mass: 질량
		self.mass = mass
		# 만약 질량이 1보다 크면 
		# 질량의 배수만큼 공의 크기를 늘려 화면에 보여준다
		self.radius = radius * self.mass
		
		# t: 현재까지 누적된 시간
		self.t = 0
		# s0: s(t=0), 즉 시간 t=0일때의 공의 초기 위치
		self.s0 = s0
		# s: 시간 t일때의 공의 위치, 즉 현재 공의 위치
		# 우선 s0로 초기화해준다
		self.s = [self.s0[0], self.s0[1]]
		# v0: v(t=0), 즉 시간 t=0일때의 공의 초기 속도
		self.v0 = v0
		# v: 시간 t일때의 속도, 즉 현재 속도
		self.v = [self.v0[0], self.v0[1]]
		# color: 물체의 색상 
		self.color = color


	# 물체에 중력 이외의 힘을 가한다
	def applyForce(self, force):
		# 뉴턴의 제 2법칙 가속도 = 힘/질량
		# 공의 가속도는 힘에 비례, 질량에 반비례함
		# 중력에 의해 발생되는 가속도는 이미  self.a에 적용되어 있음
		self.a[0] += force[0] / self.mass 
		self.a[1] += force[1] / self.mass 

	# 물체의 이전 위치에서 delta_t 초가 지난 후 위치를 구한다
	# s(t)' = s(t) +  s(delta_t)
	def computePos(self, collided_1, collided_2, delta_t=0.01):
		a = [self.a[0], self.a[1]]
		# if collided_1:
		# 	a[1] = self.a[1] - 10
		# else:
		# 	a[1] = self.a[1]
		if collided_1:
			a[1] = self.a[1] - 10
		else:
			a[1] = self.a[1]
   
   
		if collided_2:
			self.v0[0] *=  1 
			self.v0[1] *=  -0.9
		# a = 상수, 즉 등가속도 운동일 경우만 고려
		# v(t) = v0 + a*t; 여기서 v0는 이전 속도
		self.v[0] = self.v0[0] + a[0] * delta_t
		self.v[1] = self.v0[1] + a[1] * delta_t



		# s(t) = v0*t + (1/2)*a*delta^2
		#      = s0  +  s(delta_t); s는 위치, v0는 초기 속도 
		self.s[0] = self.s0[0] + (self.v[0] * delta_t)
		self.s[1] = self.s0[1] + (self.v[1] * delta_t)
		# 현재 업데이트된 속도와 위치값이 다음 delta_t
		# 에서는 초기 속도, 초기 위치값으로 세팅
		self.v0[0] = self.v[0]
		self.v0[1] = self.v[1]
		self.s0[0] = self.s[0]
		self.s0[1] = self.s[1]
  


		
		# delta_t가 지난 후 현재 시간을 업데이트한다
		self.t += delta_t
	
	def getRect(self):
		return Rect(self.s[0], self.s[1], self.size[0], self.size[1])

	def isValidPos(self, w, h):
		x = self.s[0]
		y = self.s[1]
		if x < 0 or x > w or y < 0 or y > h:
			return False
		else:
			return True
	def collide(self, other):
		# print(type(self), type(other))
		# 원과 원의 충돌 감지
		if isinstance(other, Ball):
			# dist: 유클리드 거리로 계산한 두 원의 중점 사이의 거리
			# https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%EA%B1%B0%EB%A6%AC
			dist = math.sqrt((self.s[0] - other.s[0]) ** 2 +  (self.s[1] - other.s[1]) ** 2)
			# 만약 두 중점 사이의 거리가 두 원의 반지를을 합한 것보다 작거나 같으면 
			# 충돌이 일어났다는 뜻
			if dist <= self.radius + self.radius:
				return True
			return False
		elif isinstance(other, AABB):
			
			otherRect = other.getRect()
			cx = self.s[0]
			cy = self.s[1]
			testx = cx
			testy = cy
			if cx < otherRect.left:
				testx = otherRect.left
			elif cx > otherRect.right:
				testx = otherRect.right

			if cy < otherRect.top:
				testy = otherRect.top 
			elif cy > otherRect.bottom:
				testy = otherRect.bottom
	
	
			dist_x = cx - testx
			dist_y = cy - testy
			dist = math.sqrt(dist_x ** 2 + dist_y ** 2)

			if dist <= self.radius:
				return True
			else:
				return False
				
			
			
			
