# Generated by Django 4.1.4 on 2023-02-21 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_result_r_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status',
            new_name='result_status',
        ),
    ]
