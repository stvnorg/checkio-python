from math import sqrt
class Triangle:
	a,b,c = 0,0,0
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
	def Perimeter(self):
		return self.a + self.b + self.c
	def Area(self):
		self.s = (self.a + self.b + self.c)/2
		return sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
