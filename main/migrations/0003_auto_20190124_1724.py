# Generated by Django 2.0 on 2019-01-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190124_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectcreation',
            name='course_credit',
            field=models.CharField(choices=[('C - 0.75', '0.75 Credit'), ('C - 1.00', '1.00 Credit'), ('C - 1.50', '1.50 Credit'), ('C - 2.00', '2.00 Credit'), ('C - 3.00', '3.00 Credit'), ('C - 4.00', '4.00 Credit')], max_length=4),
        ),
        migrations.AlterField(
            model_name='subjectcreation',
            name='sibject_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
