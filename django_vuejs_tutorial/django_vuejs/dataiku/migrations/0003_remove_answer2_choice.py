# Generated by Django 2.2.5 on 2020-08-31 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataiku', '0002_answer2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer2',
            name='choice',
        ),
    ]
