# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recipe.tags'
        db.delete_column(u'recipes_recipe', 'tags')


    def backwards(self, orm):
        # Adding field 'Recipe.tags'
        db.add_column(u'recipes_recipe', 'tags',
                      self.gf('tagging.fields.TagField')(default=''),
                      keep_default=False)


    models = {
        u'recipes.category': {
            'Meta': {'ordering': "['order_index']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'order_index': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'recipes.direction': {
            'Meta': {'ordering': "['order', 'id']", 'object_name': 'Direction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Recipe']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'recipes.food': {
            'Meta': {'ordering': "['name_sorted']", 'object_name': 'Food'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.FoodGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name_sorted': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'})
        },
        u'recipes.foodgroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'FoodGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'recipes.ingredient': {
            'Meta': {'ordering': "['direction', 'order_index', 'id']", 'object_name': 'Ingredient'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'amountMax': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Direction']", 'null': 'True', 'blank': 'True'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Food']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'order_index': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'prep_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.PrepMethod']", 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Recipe']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Unit']", 'null': 'True', 'blank': 'True'})
        },
        u'recipes.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keep': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Recipe']"})
        },
        u'recipes.prepmethod': {
            'Meta': {'ordering': "['-name']", 'object_name': 'PrepMethod'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        u'recipes.recipe': {
            'Meta': {'ordering': "['title']", 'object_name': 'Recipe'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Category']"}),
            'ctime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'prep_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipes.Source']", 'symmetrical': 'False', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'recipes.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'recipes.unit': {
            'Meta': {'ordering': "['name']", 'object_name': 'Unit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'plural': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'plural_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['recipes']