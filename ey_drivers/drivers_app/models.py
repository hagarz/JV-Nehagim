from django.db import models
from django.core.exceptions import ValidationError
import datetime


class Drivers(models.Model):
    driver_id = models.IntegerField('תעודת זהות', primary_key=True)
    driver_name = models.CharField("שם מלא", max_length=32)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'נהג'
        verbose_name_plural = 'נהגים'


    def __str__(self):
        return self.driver_name


class Schedule(models.Model):
    driver_id = models.ForeignKey(Drivers, on_delete=models.CASCADE,verbose_name="נהג")
    start_time = models.DateTimeField("התחלת עבודה", auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField("סיום עבודה", auto_now=False, auto_now_add=False)
    #hours_worked = models.IntegerField("number of hours worked") #,
                    # default=
                    # (datetime.datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S') -
                    #  datetime.datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S')).seconds/3600)

    def __str__(self):
        return f"{str(self.driver_id)};  תאריך: {str(self.start_time)}; שעות: {str(self.hours_worked_)}"

    @property
    def hours_worked_(self):
        verbose_name = "שעות"
        if self.start_time and self.end_time:
            time_diff = self.end_time - self.start_time
            return float(time_diff.total_seconds()/3600)

    def date(self):
        return self.start_time.date()
    date.admin_order_field = 'start_time'

    def clean(self):
        # Don't allow end_time to be before start_time.
        if self.start_time >= self.end_time and self.end_time is not None:
            raise ValidationError('זמן סיום משמרת לפני תחילת משמרת, אנא בדקי את התאריכים והשעות שהזנת ונסי שוב.')

    class Meta:
        verbose_name = 'משמרת'
        verbose_name_plural = 'משמרות'






# a primary key field will automatically be added to your model if you don’t specify otherwise
#id = models.AutoField(primary_key=True)

# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.