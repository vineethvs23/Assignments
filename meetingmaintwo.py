from meeting import MeetingManager
password="123#"
k=1
meeting=MeetingManager()
while k>0:
	word=input("\nPress enter: ")

	if word=="123#":
		print("----scheduled meetings----")
		for i,j in meeting.scheduled.items():
			print(" -",i,"-",j)
	else:
		choice=input("\nDo you want to \n1.Schedule a meeting with the manager?\n2.Reschedule your meeting with your manager?\n Your choice: ")
		if choice=='1':
			meeting.name=input("\nEnter your name: ")
			k+=1
			while True:
				option=int(input("\nEnter the option number\n1.View time slots\n2.Schedule meeting\n3.Exit\nEnter option: "))
				if option==1:
					meeting.time_view()
				elif option==2:
					meeting.schedule()
					break
					#managerdict=meeting.scheduled
				else:
					break
		else:
			Name=input("\nEnter your name:")
			searchtimeslot=input("\nEnter the time slot previously taken:")
			for timeslot in meeting.scheduled.keys():
				if timeslot==searchtimeslot:
					meeting.scheduled.pop(timeslot)
					meeting.openslots[timeslot]="Empty"
					print("\n**Your meeting has been canceled.\nYou can Reschedule now.")
					break
						