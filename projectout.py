from main.models import Project

ProjAll = Project.objects.filter(active=True)
for project in ProjAll:
	sno = str(project.id)
	print('id:'+sno+'\tName:'+project.name+'\tDescription:'+project.description)
