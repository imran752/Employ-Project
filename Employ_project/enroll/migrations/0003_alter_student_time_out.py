# Generated by Django 4.1.6 on 2023-03-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_student_time_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='time_out',
            field=models.TimeField(),
        ),
    ]
