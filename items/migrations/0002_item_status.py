# Generated by Django 4.0.4 on 2022-05-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(default='inactive', max_length=10),
        ),
    ]
