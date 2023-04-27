# Generated by Django 4.2 on 2023-04-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_attendance_system', '0018_student_feedback_status_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (3, 'STUDENT'), (2, 'STAFF')], default=1, max_length=1),
        ),
    ]