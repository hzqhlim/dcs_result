# Generated by Django 4.1.4 on 2023-02-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_status_rename_lecture_lecture_lecture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
