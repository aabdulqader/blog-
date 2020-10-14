# Generated by Django 3.1.1 on 2020-10-14 18:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20201014_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
