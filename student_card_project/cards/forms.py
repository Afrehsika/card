from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'program', 'student_number', 'nationality', 'index_no', 'validity_start', 'validity_end', 'photo']
