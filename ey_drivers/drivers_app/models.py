from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.functions import ExtractWeek, ExtractMonth, ExtractYear
from django.db.models import Sum, Count

import datetime
from datetime import timedelta
from django.db.models import F
# An F() object represents the value of a model field or annotated column.
# It makes it possible to refer to model field values and perform database operations using them without
# actually having to pull them out of the database into Python memory.
# compare the value of a model field with another field on the same model
# F() can be used to create dynamic fields on your models by combining different fields with arithmetic



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

    def __str__(self):
        return f"{str(self.driver_id)};  start_date: {str(self.start_time)}; end_date: {str(self.end_time)}; " \
               f"num_hours: {str(self.hours_worked_property)} "

    def hours_worked_(self):
        if self.start_time and self.end_time:
            time_diff = self.end_time - self.start_time
            return float(time_diff.total_seconds()/3600)
        # else:
        #     return 0
    hours_worked_.short_description = "מספר שעות"
    hours_worked_property = property(hours_worked_)

    def date(self):
        return self.start_time.date()
    date.admin_order_field = 'start_time'
    date.short_description = "תאריך"

    def clean(self):
        """ provide custom model validation, and to modify attributes on model if desired."""

        # Don't allow end_time to be before start_time.
        if self.end_time is not None and self.start_time >= self.end_time:
            raise ValidationError('זמן סיום משמרת לפני תחילת משמרת, אנא בדקי את התאריכים והשעות שהזנת ונסי שוב.')


        # Don't allow less than 7 hrs rest between shifts
        all_driver_records = Schedule.objects.filter(driver_id=self.driver_id)

        # all_driver_records = all_driver_records.objects.filter(start_time__lt=F('start_time') + timedelta(hours=3))
        if all_driver_records:
            all_driver_records_before = Schedule.objects\
                .filter(driver_id=self.driver_id, start_time__gt=self.start_time - timedelta(hours=7))\
                .exclude(start_time__gt=self.start_time)
            all_driver_records_after = Schedule.objects\
                .filter(driver_id=self.driver_id, end_time__lt=self.end_time + timedelta(hours=7, days=0))\
                .exclude(end_time__lt=self.end_time)
            print("end_time:", self.end_time)
            print("end_time_lt:", self.end_time + timedelta(hours=7, days=0))
            print("all_driver_records_before:", all_driver_records_before)
            print("all_driver_records_after:", all_driver_records_after)
            # last_record = all_driver_records[all_driver_records.count()-1]  # get last shift
            # hours_from_last_end = last_record.end_time
            # time_from_last = self.start_time - hours_from_last_end
            # if float(time_from_last.total_seconds()/3600) < 7:
            if all_driver_records_before or all_driver_records_after:
                raise ValidationError('נהג לא יתחיל את יום עבודתו בנהיגה אלא אחרי מנוחה שמחוץ לעבודה במשך 7 שעות רצופות לפחות')

            # Don't allow too many hours
            hrs_24 = []
            days_7 = []
            hrs24 = 0
            days7 = 0
            for shift in all_driver_records:
                if (self.start_time - shift.end_time).total_seconds()/3600 <= 24:
                    hrs_24.append(shift)
                    days_7.append(shift)
                    hrs24 += (self.start_time - shift.end_time).total_seconds()/3600
                    days7 += (self.start_time - shift.end_time).total_seconds()/3600
                elif (self.start_time - shift.end_time).total_seconds()/3600 <= 7*24:
                    days_7.append(shift)
                    days7 += (self.start_time - shift.end_time).total_seconds()/3600
            if hrs24 > 12:
                raise ValidationError('נהג לא ינהג יותר מ- 12 שעות בכל תקופה של 24 שעות')
            if days7 > 68:
                raise ValidationError('נהג לא ינהג יותר מ- 68 שעות בכל תקופה של 7 ימים')
            # all_hours = Schedule.objects.annotate(F('hours_worked_'))
            # print('all_hours:', all_hours)

    # def hours_per_week(self):
    #     gw = \
    #         Schedule.objects.annotate(
    #             year=ExtractYear('start_time'),
    #             week=ExtractWeek('start_time')).values('year', 'week')
    #     gw = gw.annotate(Sum('hours_worked_')).values('year', 'week', 'driver_id')
    #     for i in gw:
    #         print(i)
    #     # month = {Schedule.objects.annotate(month=ExtractMonth('start_time')).values('month').get(end_time__year=ExtractYear('start_time'))}
    #     # # print(month)
    #     # aggregate = Schedule.objects.extra(
    #     #     {"month": ExtractMonth('start_time'), "year": ExtractYear('start_time')}).values('month', 'year').annotate(
    #     #     total=Count('driver_id')).values('month', 'year', 'total')
    #     # return month
    #
    # aggregated_month_hrs_property = property(hours_per_week)

    class Meta:
        verbose_name = 'משמרת'
        verbose_name_plural = 'משמרות'





    # a primary key field will automatically be added to your model if you don’t specify otherwise
#id = models.AutoField(primary_key=True)

# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.