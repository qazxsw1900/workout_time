# Generated by Django 3.2.9 on 2021-11-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_auto_20211111_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouttimes',
            name='workout1',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout2',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout3',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout4',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workoutTotal',
            field=models.CharField(max_length=5),
        ),
    ]
