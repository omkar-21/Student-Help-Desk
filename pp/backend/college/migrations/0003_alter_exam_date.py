# Generated by Django 3.2 on 2021-04-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(),
        ),
    ]
