from todolist import ToDoList
while True:
	selection=int(input("\nEnter the task to be performed:\n1.Create a new To Do list\
		\n2.Add a new task\
	\n3.Mark task as completed\
	\n4.Display list of tasks\
	\nYour selection: "))
	if selection==1:
		userlist=ToDoList()
		userlist.ToDo()
	if selection==2:
		userlist.add()
	if selection==3:
		userlist.Markdone()
	if selection==4:
		sel=int(input("\n1.Remaining tasks\n2.Completed tasks\nYour choice: "))
		if sel==1:
			userlist.display()
		else:
			userlist.DONE_disp()	

