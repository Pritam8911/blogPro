# Generated by Django 4.0.1 on 2022-02-26 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_remove_newarrival_casting_newarrival_casting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newarrival',
            name='casting',
        ),
    ]