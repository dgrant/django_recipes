# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Maximum 120 characters', unique=True, max_length=120)),
                ('order_index', models.PositiveIntegerField(null=True, blank=True)),
                ('slug', models.SlugField(help_text=b'Automatically generated from the title', unique=True)),
            ],
            options={
                'ordering': ['order_index'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
                ('order', positions.fields.PositionField(default=-1, null=True, blank=True)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('name_sorted', models.CharField(default=b'', max_length=150)),
                ('conversion_factor', models.FloatField(null=True, blank=True)),
                ('name_plural', models.CharField(max_length=150, null=True, blank=True)),
                ('detail', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name_sorted'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(null=True, blank=True)),
                ('amountMax', models.FloatField(null=True, blank=True)),
                ('order_index', positions.fields.PositionField(default=-1, null=True, blank=True)),
                ('direction', models.ForeignKey(related_name=b'ingredients', to='recipes.Direction')),
                ('food', models.ForeignKey(to='recipes.Food')),
            ],
            options={
                'ordering': ['direction', 'order_index', 'id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'images')),
                ('keep', models.BooleanField(default=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrepMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, blank=True)),
            ],
            options={
                'ordering': ['-name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=500, blank=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('prep_time', models.CharField(max_length=100, blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('serving_value', models.IntegerField(null=True, blank=True)),
                ('category', models.ForeignKey(to='recipes.Category')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServingString',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField(max_length=500, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('name_abbrev', models.CharField(max_length=60, blank=True)),
                ('plural_abbrev', models.CharField(max_length=60, blank=True)),
                ('type', models.IntegerField(choices=[(0, b'Other'), (1, b'Mass'), (2, b'Volume')])),
                ('system', models.IntegerField(null=True, choices=[(0, b'SI'), (1, b'Imperial')])),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='serving_string',
            field=models.ForeignKey(blank=True, to='recipes.ServingString', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='sources',
            field=models.ManyToManyField(to='recipes.Source', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='recipe',
            field=models.ForeignKey(to='recipes.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='prep_method',
            field=models.ForeignKey(blank=True, to='recipes.PrepMethod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(to='recipes.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(blank=True, to='recipes.Unit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='conversion_src_unit',
            field=models.ForeignKey(related_name=b'+', blank=True, to='recipes.Unit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='group',
            field=models.ForeignKey(to='recipes.FoodGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direction',
            name='recipe',
            field=models.ForeignKey(related_name=b'directions', to='recipes.Recipe'),
            preserve_default=True,
        ),
    ]
