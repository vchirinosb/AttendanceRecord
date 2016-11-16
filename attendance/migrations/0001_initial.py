# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 21:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timeOfEntry', models.TimeField()),
                ('departureTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Solo caracteres numericos', regex='^[0-9]*$')])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Justification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='JustificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthYear', models.DateField()),
                ('leaveDays', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator(message='Solo caracteres numericos', regex='^[0-9]*$')])),
                ('unjustifAbsencesDays', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator(message='Solo caracteres numericos', regex='^[0-9]*$')])),
                ('justifAbsencesDays', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator(message='Solo caracteres numericos', regex='^[0-9]*$')])),
                ('totalDays', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='Solo caracteres numericos', regex='^[0-9]*$')])),
                ('observations', models.CharField(blank=True, max_length=250, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=70)),
                ('timeOfEntry', models.TimeField()),
                ('departureTime', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='justification',
            name='justificationType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.JustificationType'),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.Employee'),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='workingPeriod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.WorkingPeriod'),
        ),
    ]
