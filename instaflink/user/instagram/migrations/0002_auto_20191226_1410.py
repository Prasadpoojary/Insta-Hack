# Generated by Django 2.0 on 2019-12-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hacked_account',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
