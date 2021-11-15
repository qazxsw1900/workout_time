from django.db import models


class WorkoutTimes(models.Model):
    user = models.CharField(max_length=50)
    workout1 = models.DurationField(default=0)
    workout2 = models.DurationField(default=0)
    workout3 = models.DurationField(default=0)
    workout4 = models.DurationField(default=0)
    points = models.IntegerField(default=0, )

    def __str__(self):
        return self.user
