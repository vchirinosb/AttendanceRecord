from django.shortcuts import render
from django.db.models.aggregates import Sum
from django.db.models.expressions import F
from attendance.models import Employee
from attendance.forms import EmployeeFilterForm


# Create your views here.
def indexView(request):
    template_name = 'attendance/index.html'
    return render(request, template_name, {})


#####################
# Attendance Record #
#####################
def attendanceRecordList(request):
    template_name = 'attendance/attendancerecordmaint/'\
                    'attendancerecordlist.html'
    form_class = EmployeeFilterForm(request.POST or None)

    employees = Employee.objects.annotate(
        numberHours=Sum(F('attendancerecord__departureTime') -
                        F('attendancerecord__timeOfEntry')))

    totalHours = Employee.objects.aggregate(
        numberHours=Sum(F('attendancerecord__departureTime') -
                        F('attendancerecord__timeOfEntry')))

    if form_class.is_valid():
        employeeIdTmp = form_class.cleaned_data['name'].values("id")
        startDateTmp = form_class.cleaned_data['startDate']
        endDateTmp = form_class.cleaned_data['endDate']

        employees = Employee.objects.filter(
            attendancerecord__dateAttendance__range=[startDateTmp, endDateTmp],
            id__in=employeeIdTmp)\
            .annotate(numberHours=Sum(F('attendancerecord__departureTime') -
                                      F('attendancerecord__timeOfEntry')))

        totalHours = Employee.objects.filter(
            attendancerecord__dateAttendance__range=[startDateTmp, endDateTmp],
            id__in=employeeIdTmp)\
            .aggregate(numberHours=Sum(F('attendancerecord__departureTime') -
                                       F('attendancerecord__timeOfEntry')))

    context = {
        "form": form_class,
        "employees": employees,
        "totalHours": totalHours
    }

    return render(request, template_name, context)
