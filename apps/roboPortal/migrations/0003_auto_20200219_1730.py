# Generated by Django 2.1.7 on 2020-02-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboPortal', '0002_auto_20200219_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portaluser',
            name='semester',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]