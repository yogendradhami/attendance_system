# Generated by Django 4.2 on 2023-04-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_attendance_system', '0003_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(upload_to='static/img/prifile_pic'),
        ),
    ]
