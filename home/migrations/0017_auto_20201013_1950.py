# Generated by Django 3.1.1 on 2020-10-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20201013_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
