# Generated by Django 3.1.1 on 2020-10-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20201013_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]