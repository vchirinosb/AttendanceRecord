from django import forms
from attendance.models import Employee
from django.db.models.expressions import F
from django.db.models.aggregates import Sum


class EmployeeFilterForm(forms.Form):
    name = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(),
                                          required=False)
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

    def getEmployees(
            self, employeeIdTmp=None, startDateTmp=None, endDateTmp=None):
        if employeeIdTmp:
            return Employee.objects.filter(
                attendancerecord__dateAttendance__range=[
                    startDateTmp, endDateTmp], id__in=employeeIdTmp)\
                .annotate(numberHours=Sum(
                    F('attendancerecord__departureTime') -
                    F('attendancerecord__timeOfEntry')))
        else:
            return Employee.objects.annotate(
                numberHours=Sum(F('attendancerecord__departureTime') -
                                F('attendancerecord__timeOfEntry')))

    def getTotalHours(
            self, employeeIdTmp=None, startDateTmp=None, endDateTmp=None):
        if employeeIdTmp:
            return Employee.objects.filter(
                attendancerecord__dateAttendance__range=[
                    startDateTmp, endDateTmp], id__in=employeeIdTmp)\
                .aggregate(numberHours=Sum(
                    F('attendancerecord__departureTime') -
                    F('attendancerecord__timeOfEntry')))
        else:
            return Employee.objects.aggregate(
                numberHours=Sum(F('attendancerecord__departureTime') -
                                F('attendancerecord__timeOfEntry')))
