# Generated by Django 3.2 on 2021-04-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_alter_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
