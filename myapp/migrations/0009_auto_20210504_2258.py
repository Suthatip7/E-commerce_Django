# Generated by Django 2.2.5 on 2021-05-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210504_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='item2',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='item3',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]