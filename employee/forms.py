from django import forms
from .models import Employee
#DataFlair
class EmployeeCreate(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'