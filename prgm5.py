#mouse
class Pointer(object):
	def __init__(self,x,y):
		self.x=x
		#print(self.x)

		self.y=y
		#print(self.y)
	def moveup(self):
		self.y=self.y+1	
	def movedown(self):
		self.y=self.y-1	
	def moveleft(self):
		self.x=self.x-1	
	def moveright(self):
		self.x=self.x+1	
	def position(self):
		print("(",self.x,self.y,")")
						

#change
	# def func(self,x,y):
	# 	a = self.x + self.y
	# 	b = x + y
	# 	print(a)
	# 	print(b)
# variable = Pointer(10,20)
