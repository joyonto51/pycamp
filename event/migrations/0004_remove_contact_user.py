# Generated by Django 2.0.4 on 2018-04-25 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
