from django.db import models
from django.core.validators import RegexValidator


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, validators=[RegexValidator(
        regex='^[0-9]*$', message='Only numeric characters')])

    def __str__(self):
        return self.name + " " + self.last_name


class WorkingPeriod(models.Model):
    description = models.CharField(max_length=70)
    time_of_entry = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return self.description


class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    working_period = models.ForeignKey(WorkingPeriod, on_delete=models.PROTECT)
    date_attendance = models.DateField()
    time_of_entry = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return str(self.dateAttendance)


class JustificationType(models.Model):
    description = models.CharField(max_length=70)

    def __str__(self):
        return self.description


class Justification(models.Model):
    justification_type = models.ForeignKey(JustificationType,
                                           on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.startDate)


class PersonalControl(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    month_year = models.DateField()
    leave_days = models.CharField(
        max_length=2, blank=True, null=True,
        validators=[RegexValidator(regex='^[0-9]*$',
                                   message='Only numeric characters')])
    unjustif_absences_days = models.CharField(
        max_length=2, blank=True, null=True,
        validators=[RegexValidator(regex='^[0-9]*$',
                                   message='Only numeric characters')])
    justif_absences_days = models.CharField(
        max_length=2, blank=True, null=True,
        validators=[RegexValidator(regex='^[0-9]*$',
                                   message='Only numeric characters')])
    total_days = models.CharField(
        max_length=2,
        validators=[RegexValidator(regex='^[0-9]*$',
                                   message='Only numeric characters')])
    observations = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.monthYear)
