# Generated by Django 5.1.5 on 2025-02-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_number',
            field=models.IntegerField(),
        ),
    ]
