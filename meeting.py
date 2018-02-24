
class MeetingManager(object):
	"""docstring fMeetingManager"""
	def __init__(self):
		#self.owner = user
		self.openslots={'10-11':'Empty','11-12':'Empty','12-1':'Empty','1-2':'Empty','2-3':'Empty','3-4':'Empty','4-5':'Empty',
		'5-6':'Empty','6-7':'Empty'}
		self.scheduled={}
		#self.name=''
	
	def time_view(self):
		print("\n--Time slots available--")
		for i,j in self.openslots.items():
			print('-',i,"--",j)
	
	def schedule(self):
		time=input("\nEnter the time slot: ")
		if time in self.openslots.keys():
			self.scheduled[time]=self.name
			#print(self.scheduled)
			self.openslots.pop(time)
			print("\n* Your meeting has been scheduled.\n-Thank you.")
		else:
			print("\n Time slot not available. ")



		