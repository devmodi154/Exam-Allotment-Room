# Generated by Django 2.2.6 on 2019-10-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input1', '0012_auto_20191030_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='division',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
