from django.shortcuts import render
from .models import AttendanceRecord
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def IndexView(request):
    template_name = 'attendance/index.html'
    return render(request, template_name, {})

#####################
# Attendance Record #
#####################
def AttendanceRecordList(request):
    template_name = 'attendance/attendancerecordmaint/attendancerecordlist.html'
    
    global resultado
    
    attendances = AttendanceRecord.objects.all()
    
    #
    paginate_by = 10
    paginator = Paginator(attendances, paginate_by)
    
    page = request.GET.get('page')
    
    try:
        attendances = paginator.page(page)
    except PageNotAnInteger:
        attendances = paginator.page(1)
    except EmptyPage:
        attendances = paginator.page(paginator.num_pages)
    #
    
    context = { 
        "attendances": attendances
    }
    
    return render(request, template_name, context)
