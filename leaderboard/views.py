import datetime
from django.shortcuts import render
from .models import WorkoutTimes
from django.contrib import messages
from django.db.models import F
import time


def index(request):
    tic = time.perf_counter()
    workouts = WorkoutTimes.objects.all()
    top = [], [], [], []
    for i in range(4):
        for workout in workouts:
            if not (workout.__dict__[f'workout{i + 1}']) in top[i]:
                top[i].append(workout.__dict__[f'workout{i + 1}'])
        top[i].sort()
    workouts = workouts.filter().order_by(f'points')
    toc = time.perf_counter()
    print(f"Page loaded in {toc - tic:0.4f} seconds")
    return render(request, 'leaderboard/index.html',
                  {"workouts": workouts, 'top1': top[0], 'top2': top[1], 'top3': top[2], 'top4': top[3]})


def addTime(request):
    if request.method == 'POST':
        times = []
        total_sec = 0
        for i in range(4):
            times.append(int(request.POST.get(f'time{i}m', 0)) * 60 + int(request.POST.get(f'time{i}s', 0)))
            total_sec += times[-1]
        NewTime = WorkoutTimes()
        NewTime.user = request.POST.get(f'name', 'null')
        for i in range(4):
            NewTime.__dict__[f'workout{i + 1}'] = datetime.timedelta(seconds=times[i])
        NewTime.save()
        messages.success(request, 'Time successfully added')
        workouts = WorkoutTimes.objects.all()
        workouts.update(points=0)
        top = [], [], [], []
        for i in range(4):
            for workout in workouts:
                if not (workout.__dict__[f'workout{i + 1}']) in top[i]:
                    top[i].append(workout.__dict__[f'workout{i + 1}'])
            top[i].sort()
            for j in range(len(top[i])):
                if i == 0:
                    WorkoutTimes.objects.filter(workout1=top[i][j]).update(points=F('points') + j + 1)
                elif i == 1:
                    WorkoutTimes.objects.filter(workout2=top[i][j]).update(points=F('points') + j + 1)
                elif i == 2:
                    WorkoutTimes.objects.filter(workout3=top[i][j]).update(points=F('points') + j + 1)
                elif i == 3:
                    WorkoutTimes.objects.filter(workout4=top[i][j]).update(points=F('points') + j + 1)
        return render(request, 'leaderboard/newTime.html')
    else:
        return render(request, 'leaderboard/newTime.html')


def result(request):
    tic = time.perf_counter()
    workouts = WorkoutTimes.objects.all()
    workouts.update(points=0)
    top = [], [], [], []
    print(top)
    for i in range(4):
        for workout in workouts:
            if not (workout.__dict__[f'workout{i + 1}']) in top[i]:
                top[i].append(workout.__dict__[f'workout{i + 1}'])
        top[i].sort()
        for j in range(len(top[i])):
            if i == 0:
                WorkoutTimes.objects.filter(workout1=top[i][j]).update(points=F('points') + j + 1)
            elif i == 1:
                WorkoutTimes.objects.filter(workout2=top[i][j]).update(points=F('points') + j + 1)
            elif i == 2:
                WorkoutTimes.objects.filter(workout3=top[i][j]).update(points=F('points') + j + 1)
            elif i == 3:
                WorkoutTimes.objects.filter(workout4=top[i][j]).update(points=F('points') + j + 1)
    workouts = workouts.filter().order_by(f'points')
    toc = time.perf_counter()
    print(f"Page loaded in {toc - tic:0.4f} seconds")
    return render(request, 'leaderboard/index.html',
                  {"workouts": workouts, 'top1': top[0], 'top2': top[1], 'top3': top[2], 'top4': top[3]})
