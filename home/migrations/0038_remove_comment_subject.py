# Generated by Django 3.1.1 on 2020-10-16 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]
