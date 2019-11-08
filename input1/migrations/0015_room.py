# Generated by Django 2.2.6 on 2019-11-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input1', '0014_auto_20191107_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.PositiveIntegerField()),
                ('block', models.PositiveIntegerField(choices=[(1, 'AB-1'), (2, 'AB-2')])),
            ],
        ),
    ]