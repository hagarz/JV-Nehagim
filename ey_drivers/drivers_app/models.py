from django.db import models
from django.utils.formats import get_format

import datetime


class Drivers(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    driver_name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.driver_name


class Schedule(models.Model):
    driver_id = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    start_time = models.DateTimeField("התחלת עבודה", auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField("סיום עבודה", auto_now=False, auto_now_add=False)
    hours_worked = models.IntegerField("numbers of hours worked")#,
                    # default=
                    # (datetime.datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S') -
                    #  datetime.datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S')).seconds/3600)

    def __str__(self):
        return f"{str(self.driver_id)};  תאריך: {str(self.start_time)}; שעות: {str(self.hours_worked)}"

    # def num_hours_worked(self):
    #     return int(self.end_time - self.start_time)




# a primary key field will automatically be added to your model if you don’t specify otherwise
#id = models.AutoField(primary_key=True)

# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.