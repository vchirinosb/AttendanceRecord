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
    template_name = 'attendance/attendancerecordmaint/attendancerecordlist.html'
    form_class = EmployeeFilterForm(request.POST or None)
    
    #attendances = AttendanceRecord.objects.all()
    
    employees = Employee.objects.annotate(numberHours=Sum(F('attendancerecord__departureTime') - 
                                                          F('attendancerecord__timeOfEntry')))
    
    context = { 
        "form": form_class,
        "employees": employees
    }
    
    return render(request, template_name, context)
