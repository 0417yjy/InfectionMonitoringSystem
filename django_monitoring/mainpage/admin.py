from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(RegionLarge)
admin.site.register(RegionMedium)
#admin.site.register(RegionSmall)
admin.site.register(Subscriber)
#admin.site.register(Facility)
admin.site.register(Infected)
admin.site.register(InfectedMovement)
admin.site.register(StatisticValues)