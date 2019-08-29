# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-13 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0014_data_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this view.', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='view',
            name='help_lang1',
            field=models.TextField(blank=True, help_text='The help text for this view in the primary language.', verbose_name='Help (primary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='help_lang2',
            field=models.TextField(blank=True, help_text='The help text for this view in the secondary language.', verbose_name='Help (secondary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='help_lang3',
            field=models.TextField(blank=True, help_text='The help text for this view in the tertiary language.', verbose_name='Help (tertiary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='help_lang4',
            field=models.TextField(blank=True, help_text='The help text for this view in the quaternary language.', verbose_name='Help (quaternary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='help_lang5',
            field=models.TextField(blank=True, help_text='The help text for this view in the quinary language.', verbose_name='Help (quinary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this view.', max_length=128, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='view',
            name='template',
            field=models.TextField(blank=True, help_text='The template for this view, written in Django template language.', verbose_name='Template'),
        ),
        migrations.AlterField(
            model_name='view',
            name='title_lang1',
            field=models.CharField(blank=True, help_text='The title for this view in the primary language.', max_length=256, verbose_name='Title (primary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='title_lang2',
            field=models.CharField(blank=True, help_text='The title for this view in the secondary language.', max_length=256, verbose_name='Title (secondary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='title_lang3',
            field=models.CharField(blank=True, help_text='The title for this view in the tertiary language.', max_length=256, verbose_name='Title (tertiary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='title_lang4',
            field=models.CharField(blank=True, help_text='The title for this view in the quaternary language.', max_length=256, verbose_name='Title (quaternary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='title_lang5',
            field=models.CharField(blank=True, help_text='The title for this view in the quinary language.', max_length=256, verbose_name='Title (quinary)'),
        ),
        migrations.AlterField(
            model_name='view',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this view (auto-generated).', max_length=640, verbose_name='URI'),
        ),
        migrations.AlterField(
            model_name='view',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this view.', max_length=256, verbose_name='URI Prefix'),
        ),
    ]