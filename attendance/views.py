from django.shortcuts import render
from attendance.forms import EmployeeFilterForm


def index_view(request):
    template_name = 'attendance/index.html'
    return render(request, template_name, {})


def attendance_record_list(request):
    template_name = 'attendance/attendancerecordmaint/'\
                    'attendancerecordlist.html'

    form_class = EmployeeFilterForm(request.POST or None)

    employees = EmployeeFilterForm.get_employees(form_class)
    total_hours = EmployeeFilterForm.get_total_hours(form_class)

    context = {
        "form": form_class,
        "employees": employees,
        "total_hours": total_hours
    }

    return render(request, template_name, context)
