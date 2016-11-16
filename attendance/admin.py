from django.contrib import admin
from attendance.models import Department, Employee, WorkingPeriod, AttendanceRecord ,\
    JustificationType, Justification, PersonalControl

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Department


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Employee


class WorkingPeriodAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = WorkingPeriod


class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ["__str__", "employee"]
    class Meta:
        model = AttendanceRecord


class JustificationTypeAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = JustificationType


class JustificationAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Justification


class PersonalControlAdmin(admin.ModelAdmin):
    list_display = ["__str__", "employee"]
    class Meta:
        model = PersonalControl


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(WorkingPeriod, WorkingPeriodAdmin)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)
admin.site.register(JustificationType, JustificationTypeAdmin)
admin.site.register(Justification, JustificationAdmin)
admin.site.register(PersonalControl, PersonalControlAdmin)
