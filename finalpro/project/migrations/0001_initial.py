# Generated by Django 4.1.4 on 2023-02-15 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('LectID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('LectName', models.TextField()),
                ('LectPass', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudID', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('StudName', models.TextField()),
                ('StudIC', models.CharField(max_length=12)),
                ('StudPass', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.TextField()),
                ('r_ic', models.CharField(max_length=12)),
                ('r_prog', models.TextField(default='DIPLOMA IN COMPUTER SCIENCE')),
                ('r_session', models.CharField(default='SESSION 3 2022/2023', max_length=19)),
                ('r_desc', models.TextField()),
                ('r_grade', models.TextField()),
                ('r_kredit', models.TextField()),
                ('r_status', models.CharField(max_length=12)),
                ('r_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.subject')),
                ('r_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.student')),
            ],
        ),
    ]
