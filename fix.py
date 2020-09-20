from main.models import Project
lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat'

for i in range(2,10):
	name = 'Project'+str(i)
	Project.objects.create(name=name,description=lorem)
	print('object'+str(i)+'created')
print('Object creations completed')

ProjAll = Project.objects.filter(active=True)
for project in ProjAll:
	sno = str(project.id)
	print('id:'+sno+'\tName:'+project.name+'\tDescription:'+project.description)
