# Generated by Django 3.2.9 on 2021-11-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0008_rename_workouttotal_workouttimes_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouttimes',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout1',
            field=models.DurationField(default=0),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout2',
            field=models.DurationField(default=0),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout3',
            field=models.DurationField(default=0),
        ),
        migrations.AlterField(
            model_name='workouttimes',
            name='workout4',
            field=models.DurationField(default=0),
        ),
    ]