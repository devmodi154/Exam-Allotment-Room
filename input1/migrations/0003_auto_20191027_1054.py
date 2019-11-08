# Generated by Django 2.2.6 on 2019-10-27 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input1', '0002_booking_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A&L', 'Arts and Law'), ('DES', 'Design'), ('ENG', 'Engineering'), ('SCI', 'Science'), ('M&C', 'Management and Commerce')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A&L', 'Arts and Law'), ('DES', 'Design'), ('ENG', 'Engineering'), ('SCI', 'Science'), ('M&C', 'Management and Commerce')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A&L', 'Arts and Law'), ('DES', 'Design'), ('ENG', 'Engineering'), ('SCI', 'Science'), ('M&C', 'Management and Commerce')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A&L', 'Arts and Law'), ('DES', 'Design'), ('ENG', 'Engineering'), ('SCI', 'Science'), ('M&C', 'Management and Commerce')], max_length=3)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.Division')),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='course_code',
        ),
        migrations.AddField(
            model_name='faculty',
            name='designation',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='block',
            field=models.PositiveIntegerField(choices=[(1, 'AB-1'), (2, 'AB-2')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(max_length=256),
        ),
        migrations.AlterField(
            model_name='booking',
            name='faculty_assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.Faculty'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_no',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='semester',
            field=models.PositiveIntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VIII')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(max_length=256),
        ),
        migrations.AlterField(
            model_name='course',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.Branch'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(choices=[('A&L', 'Arts and Law'), ('DES', 'Design'), ('ENG', 'Engineering'), ('SCI', 'Science'), ('M&C', 'Management and Commerce')], max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.Department'),
        ),
        migrations.AlterField(
            model_name='course',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.Division'),
        ),
        migrations.AlterField(
            model_name='course',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.School'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.Division'),
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.School'),
        ),
        migrations.AddField(
            model_name='branch',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input1.Department'),
        ),
    ]