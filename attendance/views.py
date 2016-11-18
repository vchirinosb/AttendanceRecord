from django.shortcuts import render
from attendance.forms import EmployeeFilterForm


def indexView(request):
    template_name = 'attendance/index.html'
    return render(request, template_name, {})


def attendanceRecordList(request):
    template_name = 'attendance/attendancerecordmaint/'\
                    'attendancerecordlist.html'
    form_class = EmployeeFilterForm(request.POST or None)

    employees = EmployeeFilterForm.getEmployees(EmployeeFilterForm)
    totalHours = EmployeeFilterForm.getTotalHours(EmployeeFilterForm)

    if form_class.is_valid():
        employeeIdTmp = form_class.cleaned_data['name'].values("id")
        startDateTmp = form_class.cleaned_data['startDate']
        endDateTmp = form_class.cleaned_data['endDate']

        employees = EmployeeFilterForm.getEmployees(
            EmployeeFilterForm, employeeIdTmp, startDateTmp, endDateTmp)

        totalHours = EmployeeFilterForm.getTotalHours(
            EmployeeFilterForm, employeeIdTmp, startDateTmp, endDateTmp)

    context = {
        "form": form_class,
        "employees": employees,
        "totalHours": totalHours
    }

    return render(request, template_name, context)
