# Generated by Django 5.0.2 on 2024-12-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftpapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mobile_number',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
