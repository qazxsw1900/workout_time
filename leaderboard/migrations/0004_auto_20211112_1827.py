# Generated by Django 3.2.9 on 2021-11-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_auto_20211111_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouttimes',
            name='user',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout1',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout2',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout3',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout4',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workoutTotal',
            field=models.FloatField(max_length=5),
        ),
    ]
