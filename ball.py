import math

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
class Ball:
	def __init__(self, mass=1, s0=[0, 0], v0=[0, 0], a=[0, 0], radius=10, 	color=WHITE):
		# g: 중력가속도 9.8m/s^2
		self.g = [0, 9.8]
		# 합성 가속도
		self.a = [self.g[0], self.g[1]]

		#질량
		self.mass = mass

		# 반지름
		self.radius = radius * self.mass

		# t:현재까지 누적된 시뮬레이션 시간
		self.t = 0

		# v0: v(T=0), 즉 시간이 T=0초일때 초기 속도
		self.v0 = v0

		# v: v(T=t), 즉 시간이 T=t초일때 속도 (현재 속도)
		self.v = [self.v0[0], self.v0[1]]

		# s0: s(T=0), 즉 시간이 T=0초일대 초기 위치
		self.s0 = s0

		# s: s(T=t), 즉 시간이 T=t초일때 위치 (현재 위치)
		self.s = [self.s0[0], self.s0[1]]

		# color: 공 객체의 색상
		self.color = color

	# dt 초가 지난후 공 객체의 위치가 얼마나 이동했는지 
	# 계산해서 새로운 위치로 갱신하는 함수
	def computePos(self, dt=0.01):
		# a = 상수, 등가속도 운동만 고려
		# dt가 지난 후 현재 속도 = v(t + dt)
		# = v(t) + a * dt; 여기서 v(t)는 이전 속도= v0에 저장되어있음
		self.v[0] = self.v0[0] + self.a[0] * dt
		self.v[1] = self.v0[1] + self.a[1] * dt
		# dt가 지난 후 현재 위치 = s(t + dt)
		# s(dt) = v0*dt + (1/2)*a*(dt)^2 = s(t) + s(dt)
		# s(t): s0에 들어있음
		# s(t+dt): s에 해당
		# s(dt): ds에 해당
		ds_x =  self.v0[0] * dt + (1/2) * self.a[0] * (dt*dt)
		ds_y =  self.v0[1] * dt + (1/2) * self.a[1] * (dt*dt)
		self.s[0] = self.s0[0] + ds_x
		self.s[1] = self.s0[1] + ds_y

		# 업데이트된 현재 속도 v와 현재 위치 s가
		# 다음 dt가 흘렀을 때 초기(이전) 속도 v0와 초기(이전) 위치 s0로
		# 각각 사용될 수 있도록 저장해둡니다
		self.v0[0] = self.v[0] 
		self.v0[1] = self.v[1]
		self.s0[0] = self.s[0]
		self.s0[1] = self.s[1]
		# 마지막으로 현재 누적시간도 업데이트 해줍시다
		self.t += dt

	# 공 객체에 중력 이외에
	# 별도의 외력이 작용해서 물체의 운동을 변화시키는
	# 함수를 한번 추가해보겠습니다
	def applyForce(self, force):
		# new_a: 외력으로 발생한 가속도
		new_a = [0, 0]

		# 뉴턴의 제2법칙 (F = ma)에 의해서
		# 물체의 가속도는 외력의 힘에 비례하고
		# 질량에 반비례합니다
		new_a[0] = force[0] / self.mass
		new_a[1] = force[1] / self.mass

		# 중력에 의해 발생되는 가속도는
		# 이미 self.a에 적용되어 있습니다
		# 물체의 원래 가속도에 새로운 외력으로 발생한
		# 가속도만 더해주면 끝!
		self.a[0] += new_a[0]
		self.a[1] += new_a[1]

	
	# 공 객체와 다른 공 객체의 충돌을 감지하겠습니다
	def collide(self, other):
		# oter는 자신 객체와 충돌을 검사할 다른 공 객체를 
		# 가리킵니다.
		# 원-원 충돌 감지 알고리즘을 사용
		# 두 원 사이의 유클리드 거리 dist
		# dist = sqrt(dist_x^2 + dist_y^2)
		# 만약 dist 두 원의 반지름의 합보다 작거나 같다면
		# 충돌난 것으로 판정
		dist_x = self.s[0] - other.s[0]
		dist_y = self.s[1] - other.s[1]
		dist = math.sqrt(dist_x ** 2 + dist_y ** 2) 
		if dist <= (self.radius + self.radius):
			return True
		return False







	