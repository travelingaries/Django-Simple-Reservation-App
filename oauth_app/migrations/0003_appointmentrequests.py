# Generated by Django 3.1.7 on 2021-04-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0002_appointments'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.EmailField(max_length=254)),
                ('student', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
