from django import forms
from .models import Project

class ProjectAddForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('name','description')

	def __str__(self):
		return self.name
