# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-13 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_flag', models.CharField(max_length=4, verbose_name='\u5220\u9664\u6807\u5fd7')),
                ('ip', models.GenericIPAddressField(verbose_name='\u670d\u52a1\u5668ip')),
                ('createTime', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
