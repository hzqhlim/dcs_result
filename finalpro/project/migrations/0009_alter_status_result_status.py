# Generated by Django 4.1.4 on 2023-02-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_result_r_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='result_status',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
