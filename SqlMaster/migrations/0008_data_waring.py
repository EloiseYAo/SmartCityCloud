# Generated by Django 2.1.5 on 2019-02-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SqlMaster', '0007_remove_system_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='waring',
            field=models.BooleanField(default=0, verbose_name='正常/异常'),
        ),
    ]
