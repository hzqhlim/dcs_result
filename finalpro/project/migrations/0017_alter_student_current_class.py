# Generated by Django 4.1.4 on 2023-02-25 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_alter_student_current_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_class',
            field=models.ForeignKey(default='DCS 4A', on_delete=django.db.models.deletion.CASCADE, to='project.lecture'),
        ),
    ]
