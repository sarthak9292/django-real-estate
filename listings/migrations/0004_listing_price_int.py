# Generated by Django 3.2.2 on 2021-05-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210519_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price_int',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
