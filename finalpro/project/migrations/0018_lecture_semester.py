# Generated by Django 4.1.4 on 2023-02-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_alter_student_current_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='semester',
            field=models.CharField(default='INDUSTRIAL TRAINING', max_length=20),
        ),
    ]
