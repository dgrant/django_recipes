
from south.db import db
from django.db import models
from recipes.models import *

class Migration:
   
    no_dry_run = True

    def forwards(self, orm):
        "Write your forwards migration here"
        for food in orm.Food.objects.all():
            try:
                food.name_sorted = food.name
            except ValueError:
                food.name_sorted = ""
            food.save()
    
    def backwards(self, orm):
        "Write your backwards migration here"
    
    
    models = {
        'recipes.source': {
            'Meta': {'ordering': '["name"]'},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'url': ('models.URLField', [], {'max_length': '500', 'blank': 'True'})
        },
        'recipes.category': {
            'Meta': {'ordering': '["order_index"]'},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'order_index': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'unique': 'True'})
        },
        'recipes.recipe': {
            'Meta': {'ordering': "['title']"},
            'category': ('models.ForeignKey', ["orm['recipes.Category']"], {}),
            'ctime': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'mtime': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'prep_time': ('models.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'False', 'blank': 'False'}),
            'sources': ('models.ManyToManyField', ["orm['recipes.Source']"], {'blank': 'True'}),
            'summary': ('models.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'tags': ('TagField', [], {}),
            'title': ('models.CharField', [], {'max_length': '50'})
        },
        'recipes.food': {
            'Meta': {'ordering': '["name_sorted",]'},
            'group': ('models.ForeignKey', ["orm['recipes.FoodGroup']"], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'name_sorted': ('models.CharField', [], {'max_length': '150'})
        },
        'recipes.prepmethod': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        'recipes.unit': {
            'Meta': {'ordering': '["name"]'},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '60'}),
            'name_abbrev': ('models.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'plural': ('models.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'plural_abbrev': ('models.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'type': ('models.IntegerField', [], {})
        },
        'recipes.photo': {
            'caption': ('models.CharField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {}),
            'keep': ('models.BooleanField', [], {'default': 'True', 'editable': 'False'}),
            'recipe': ('models.ForeignKey', ["orm['recipes.Recipe']"], {})
        },
        'recipes.foodgroup': {
            'Meta': {'ordering': '["name"]'},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'})
        },
        'recipes.direction': {
            'Meta': {'ordering': "['order','id']"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'order': ('PositionField', [], {'null': 'True', 'unique_for_field': "'recipe'", 'blank': 'True'}),
            'recipe': ('models.ForeignKey', ["orm['recipes.Recipe']"], {}),
            'text': ('models.TextField', [], {'blank': 'True'})
        },
        'recipes.ingredient': {
            'Meta': {'ordering': '["direction","order_index","id"]'},
            'amount': ('models.FloatField', [], {}),
            'amountMax': ('models.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('models.ForeignKey', ["orm['recipes.Direction']"], {'null': 'True', 'blank': 'True'}),
            'food': ('models.ForeignKey', ["orm['recipes.Food']"], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'order_index': ('PositionField', [], {'null': 'True', 'unique_for_field': '"direction"', 'blank': 'True'}),
            'prep_method': ('models.ForeignKey', ["orm['recipes.PrepMethod']"], {'null': 'True', 'blank': 'True'}),
            'recipe': ('models.ForeignKey', ["orm['recipes.Recipe']"], {}),
            'unit': ('models.ForeignKey', ["orm['recipes.Unit']"], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['recipes']
