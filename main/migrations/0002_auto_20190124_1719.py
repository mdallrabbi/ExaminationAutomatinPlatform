# Generated by Django 2.0 on 2019-01-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectcreation',
            name='course_credit',
            field=models.CharField(choices=[('0.75', '0.75 Credit'), ('1.00', '1.00 Credit'), ('1.50', '1.50 Credit'), ('2.00', '2.00 Credit'), ('3.00', '3.00 Credit'), ('4.00', '4.00 Credit')], max_length=4),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='teachers_university',
            field=models.CharField(max_length=40),
        ),
    ]
