from django.shortcuts import render
from attendance.forms import EmployeeFilterForm


def indexView(request):
    template_name = 'attendance/index.html'
    return render(request, template_name, {})


def attendanceRecordList(request):
    template_name = 'attendance/attendancerecordmaint/'\
                    'attendancerecordlist.html'

    form_class = EmployeeFilterForm(request.POST or None)

    employees = EmployeeFilterForm.getEmployees(form_class)
    totalHours = EmployeeFilterForm.getTotalHours(form_class)

    context = {
        "form": form_class,
        "employees": employees,
        "totalHours": totalHours
    }

    return render(request, template_name, context)
