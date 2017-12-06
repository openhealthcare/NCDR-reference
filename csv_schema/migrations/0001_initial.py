# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('data_item', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('data_type', models.CharField(choices=[('datetime', 'datetime'), ('date', 'date'), ('int', 'int'), ('bigint', 'bigint'), ('varchar(1)', 'varchar(1)'), ('varchar(2)', 'varchar(2)'), ('varchar(3)', 'varchar(3)'), ('varchar(4)', 'varchar(4)'), ('varchar(5)', 'varchar(5)'), ('varchar(6)', 'varchar(6)'), ('varchar(7)', 'varchar(7)'), ('varchar(8)', 'varchar(8)'), ('varchar(9)', 'varchar(9)'), ('varchar(10)', 'varchar(10)'), ('varchar(11)', 'varchar(1)1'), ('varchar(12)', 'varchar(12)'), ('varchar(13)', 'varchar(13)'), ('varchar(14)', 'varchar(14)'), ('varchar(15)', 'varchar(15)'), ('varchar(16)', 'varchar(16)'), ('varchar(17)', 'varchar(17)'), ('varchar(18)', 'varchar(18)'), ('varchar(19)', 'varchar(19)'), ('varchar(20)', 'varchar(20)'), ('varchar(50)', 'varchar(50)'), ('varchar(100)', 'varchar(100)')], max_length=255)),
                ('derivation', models.TextField(blank=True, default='')),
                ('technical_check', models.CharField(blank=True, max_length=255, null=True)),
                ('is_derived_item', models.NullBooleanField(default=False)),
                ('definition_id', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date_ext', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(default='')),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DataDictionaryReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_schema.Column')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SiteDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('is_table', models.BooleanField(default=True)),
                ('date_range', models.CharField(blank=True, default='', max_length=255)),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_schema.Database')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='column',
            name='table',
            field=models.ManyToManyField(to='csv_schema.Table'),
        ),
        migrations.AlterUniqueTogether(
            name='table',
            unique_together=set([('name', 'database')]),
        ),
        migrations.AlterUniqueTogether(
            name='datadictionaryreference',
            unique_together=set([('column', 'name')]),
        ),
    ]
