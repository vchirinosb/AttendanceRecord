from django.shortcuts import render
from .models import AttendanceRecord
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.aggregates import Sum
from django.db.models.expressions import F
from attendance.models import Employee


# Create your views here.
def IndexView(request):
    template_name = 'attendance/index.html'
    return render(request, template_name, {})

#####################
# Attendance Record #
#####################
def AttendanceRecordList(request):
    template_name = 'attendance/attendancerecordmaint/attendancerecordlist.html'
    
    #attendances = AttendanceRecord.objects.all()
    
    employees = Employee.objects.annotate(numberHours=Sum(F('attendancerecord__departureTime') - 
                                                          F('attendancerecord__timeOfEntry')))
    
    context = { 
        "employees": employees
    }
    
    return render(request, template_name, context)
