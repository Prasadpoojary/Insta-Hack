# Generated by Django 2.0 on 2019-12-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_feadback_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feadback',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]