# Generated by Django 3.2.9 on 2021-12-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_candidate_work_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='start',
            field=models.DateField(null=True),
        ),
    ]
