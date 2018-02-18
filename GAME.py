import random
class ConsoleGame(object):
	def __init__(self):
		self.row=[]
		self.board=[]
		self.text='\n You won! :)'
	
	def generate(self):
		for j in range(8):
			for i in range(8):
				iter=random.randint(0,100)
				self.row.append(iter)
			self.board.append(self.row)
			self.row=[]	

	def choice(self):
		self.number=int(input("\nEnter your number: "))	
	
	def run(self):
		for row in self.board:
			if self.number in row:#j=0
		#for t in range(8):
		#	for i in self.row[j]:
		#		if self.number==i:
				self.text="\nYou lost! :P"
			
			#j+=1
		print(self.text)	
		for i in self.board:
			print(i,'\n')

			
				
#item=ConsoleGame()
#item.generate()
				


 