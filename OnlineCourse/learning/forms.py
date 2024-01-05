from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentForm(UserCreationForm):
    gen = (('MALE', 'Male'), ('FEMALE', 'Female'))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gen)
    qq = (('UG', 'Under Graduate'), ('PG', 'Post Graduate'), ('OTHERS', 'Others'))
    qualification = forms.ChoiceField(widget=forms.Select, choices=qq)
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Student
        fields = ['first_name', 'gender', 'qualification', 'date_of_birth', 'photo', 'username', 'password1', 'password2']
