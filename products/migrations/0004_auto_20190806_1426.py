# Generated by Django 2.2.4 on 2019-08-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190806_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='description',
            field=models.TextField(default='Add some description'),
        ),
    ]
