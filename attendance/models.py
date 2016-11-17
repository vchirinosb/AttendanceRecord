from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]*$', message='Solo caracteres numericos')])
    
    def __str__(self):
        return self.name + " " + self.lastName


class WorkingPeriod(models.Model):
    description = models.CharField(max_length=70)
    timeOfEntry = models.TimeField()
    departureTime = models.TimeField()
    
    def __str__(self):
        return self.description


class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    workingPeriod = models.ForeignKey(WorkingPeriod, on_delete=models.PROTECT)
    dateAttendance = models.DateField()
    timeOfEntry = models.TimeField()
    departureTime = models.TimeField()
    
    def __str__(self):
        return str(self.dateAttendance)


class JustificationType(models.Model):
    description = models.CharField(max_length=70)
    
    def __str__(self):
        return self.description


class Justification(models.Model):
    justificationType = models.ForeignKey(JustificationType, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    startDate = models.DateField()
    endDate = models.DateField()
    
    def __str__(self):
        return str(self.startDate)


class PersonalControl(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    monthYear = models.DateField()
    leaveDays = models.CharField(max_length=2, blank=True, null=True, validators=[RegexValidator(regex='^[0-9]*$', message='Solo caracteres numericos')])
    unjustifAbsencesDays = models.CharField(max_length=2, blank=True, null=True, validators=[RegexValidator(regex='^[0-9]*$', message='Solo caracteres numericos')])
    justifAbsencesDays = models.CharField(max_length=2, blank=True, null=True, validators=[RegexValidator(regex='^[0-9]*$', message='Solo caracteres numericos')])
    totalDays = models.CharField(max_length=2, validators=[RegexValidator(regex='^[0-9]*$', message='Solo caracteres numericos')])
    observations = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return str(self.monthYear)
