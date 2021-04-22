# Generated by Django 2.2 on 2021-04-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=15)),
                ('college', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=50)),
                ('sem', models.CharField(max_length=50)),
                ('reason', models.TextField(default='', max_length=500)),
                ('rating', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('whatsapp', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=30)),
                ('semester', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=200)),
                ('intro', models.TextField(max_length=1000)),
                ('other_club_committee', models.TextField(max_length=1000)),
                ('strength_weakness', models.TextField(max_length=1000)),
                ('work', models.TextField(max_length=1000)),
                ('why_robotix', models.TextField(max_length=1000)),
                ('improvements_suggesions', models.TextField(max_length=1000)),
                ('residence', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=5)),
                ('priority_reason', models.TextField(max_length=1000)),
                ('task_completion', models.CharField(max_length=5)),
                ('task_completion_reason', models.TextField(max_length=1000)),
                ('intention', models.CharField(max_length=5)),
                ('intention_reason', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
            ],
        ),
    ]
