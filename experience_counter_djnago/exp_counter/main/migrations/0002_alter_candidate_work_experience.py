# Generated by Django 3.2.9 on 2021-12-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='work_experience',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]