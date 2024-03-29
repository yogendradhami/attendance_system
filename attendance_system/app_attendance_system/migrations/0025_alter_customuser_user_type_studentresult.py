# Generated by Django 4.2 on 2023-04-27 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_attendance_system', '0024_rename_attendace_id_attendance_report_attendance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'STAFF'), (3, 'STUDENT')], default=1, max_length=1),
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_mark', models.IntegerField()),
                ('exam_mark', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_attendance_system.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_attendance_system.subject')),
            ],
        ),
    ]
