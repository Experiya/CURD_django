# Generated by Django 2.1.7 on 2020-12-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0006_auto_20201229_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
