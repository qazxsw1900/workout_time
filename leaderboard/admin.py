from django.contrib import admin
from .models import WorkoutTimes


class WorkoutTimesAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout1', 'workout2', 'workout3', 'workout4')

admin.site.register(WorkoutTimes, WorkoutTimesAdmin,)
