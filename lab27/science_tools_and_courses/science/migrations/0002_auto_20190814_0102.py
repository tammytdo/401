# Generated by Django 2.2.4 on 2019-08-14 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tool',
            unique_together={('tool_name', 'course')},
        ),
    ]
