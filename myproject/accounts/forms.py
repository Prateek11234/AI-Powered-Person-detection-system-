from django import forms
from .models import Enrollment

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['full_name', 'date_of_birth', 'gender', 'identification', 'address', 'state', 'pincode', 'additional_info']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Updated to match model field
        }