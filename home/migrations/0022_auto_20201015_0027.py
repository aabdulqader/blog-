# Generated by Django 3.1.1 on 2020-10-14 18:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20201015_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
