# Generated by Django 3.1.1 on 2020-10-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20201013_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='-----', max_length=200),
        ),
    ]
