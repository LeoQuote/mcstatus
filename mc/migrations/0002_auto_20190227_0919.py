# Generated by Django 2.1.7 on 2019-02-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='last_checked_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='last_started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]