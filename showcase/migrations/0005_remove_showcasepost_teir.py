# Generated by Django 3.0.8 on 2020-07-04 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0004_auto_20200704_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showcasepost',
            name='teir',
        ),
    ]