# Generated by Django 3.1.1 on 2020-10-16 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]