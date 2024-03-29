# Generated by Django 2.2.6 on 2019-10-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input1', '0003_auto_20191027_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(choices=[('A&L', 'b1'), ('DES', 'b2'), ('ENG', 'b3'), ('SCI', 'b4'), ('M&C', 'b5')], max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(choices=[('A&L', 'c1'), ('DES', 'c2'), ('ENG', 'c3'), ('SCI', 'c4'), ('M&C', 'c5')], max_length=3),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('A&L', 'd1'), ('DES', 'd2'), ('ENG', 'd3'), ('SCI', 'd4'), ('M&C', 'd5')], max_length=3),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(choices=[('A&L', 's1'), ('DES', 's2'), ('ENG', 's3'), ('SCI', 's4'), ('M&C', 's5')], max_length=3),
        ),
    ]
