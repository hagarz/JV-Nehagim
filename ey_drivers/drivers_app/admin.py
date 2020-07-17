from django.contrib import admin
from .models import Drivers
from .models import Schedule

admin.site.register(Drivers)
admin.site.register(Schedule)

