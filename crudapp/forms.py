from django import forms
from .models import Student


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll', 'full_name', 'email', 'password']
        # fields = '__all__'

        widgets = {
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value="True", attrs={'class': 'form-control'}),
        }

