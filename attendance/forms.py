'''
Created on 17 nov. 2016

@author: Hugo
'''
from django import forms
from attendance.models import Employee


class EmployeeFilterForm(forms.Form):
    
    name = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(), required=False)
    startDate = forms.DateField(required=False)
    endDate = forms.DateField(required=False)

    class Meta:
        model = Employee
        fields = ("name", "lastName")
    
    def __init__(self, *args, **kwargs):
        super(EmployeeFilterForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
        self.fields['name'].label = "Select Employees"
        self.fields['startDate'].label = "From"
        self.fields['endDate'].label = "To"
