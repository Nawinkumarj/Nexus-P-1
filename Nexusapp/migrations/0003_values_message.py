# Generated by Django 5.0.1 on 2024-06-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nexusapp', '0002_values_delete_datas'),
    ]

    operations = [
        migrations.AddField(
            model_name='values',
            name='message',
            field=models.CharField(default='', max_length=100),
        ),
    ]