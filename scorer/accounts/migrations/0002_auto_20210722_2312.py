# Generated by Django 3.2.4 on 2021-07-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='examtime',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='gktime',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='mattime',
            field=models.IntegerField(default=100),
        ),
    ]
