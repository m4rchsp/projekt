# Generated by Django 4.0.4 on 2022-05-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_thumb',
            field=models.TextField(),
        ),
    ]