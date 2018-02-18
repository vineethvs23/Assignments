#table={}
#done={}
class ToDoList(object):
	def __init__():
		self.table={}
		self.done={}
	def ToDo(self):
		self.name=input("\nEnter the name of the To Do list:")
		table[self.name]=[]
	
	def add(self):
		self.task=input("\nEnter the task to be added:")
		table[self.name].append(self.task)	
	
	def Markdone(self):
		self.find=input("\nEnter the task name:")
		for i in table[self.name]:
			if i==self.find:
				done[self.name]=[i]
				table[self.name].remove(i)
			
	def display(self):
		print('\n','----',self.name,'----')
		for i in table[self.name]:
			print("\n-",i)
		print("  ----END----")
					
	def DONE_disp(self):
		print('\n','----DONE TASKS of',self.name,'----')
		for i in done[self.name]:
			print('\n-',i)
		print("  ----END----")			
