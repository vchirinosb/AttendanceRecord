from django import forms
from attendance.models import Employee
from django.db.models.expressions import F
from django.db.models.aggregates import Sum


class EmployeeFilterForm(forms.Form):
    name = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(),
                                          required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

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
        self.fields['start_date'].label = "From"
        self.fields['end_date'].label = "To"

    def get_employees(self):
        if self.is_valid():
            return (Employee.objects.filter(
                attendancerecord__date_attendance__range=[
                    self.cleaned_data['start_date'],
                    self.cleaned_data['end_date']], id__in=self.cleaned_data[
                        'name'].values("id"))
                    .annotate(number_hours=Sum(
                        F('attendancerecord__departure_time') -
                        F('attendancerecord__time_of_entry'))))
        else:
            return Employee.objects.annotate(
                number_hours=Sum(F('attendancerecord__departure_time') -
                                 F('attendancerecord__time_of_entry')))

    def get_total_hours(self):
        if self.is_valid():
            return (Employee.objects.filter(
                attendancerecord__date_attendance__range=[
                    self.cleaned_data['start_date'],
                    self.cleaned_data['end_date']], id__in=self.cleaned_data[
                        'name'].values("id"))
                    .aggregate(number_hours=Sum(
                        F('attendancerecord__departure_time') -
                        F('attendancerecord__time_of_entry'))))
        else:
            return Employee.objects.aggregate(
                number_hours=Sum(F('attendancerecord__departure_time') -
                                 F('attendancerecord__time_of_entry')))
