# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0002_item_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='it_cate',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_code',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_contact',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_drive_num',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_get_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_get_nm',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_get_place',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_get_position',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_get_thing',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_image_url',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_status',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_take_place',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_title',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='it_url',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
