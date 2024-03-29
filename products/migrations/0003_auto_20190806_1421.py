# Generated by Django 2.2.4 on 2019-08-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190806_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='image',
            field=models.FileField(default=None, max_length=150, upload_to='deals'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='is_published',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='deal',
            name='published_date',
            field=models.DateField(default=None),
        ),
    ]
