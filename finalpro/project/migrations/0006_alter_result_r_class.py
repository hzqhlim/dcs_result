# Generated by Django 4.1.4 on 2023-02-21 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_status_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='r_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.lecture'),
        ),
    ]
