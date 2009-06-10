
from south.db import db
from django.db import models
from recipes.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Source'
        db.create_table('recipes_source', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=150)),
            ('url', models.URLField(max_length=500, blank=True)),
        ))
        db.send_create_signal('recipes', ['Source'])
        
        # Adding model 'Category'
        db.create_table('recipes_category', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(unique=True, max_length=120)),
            ('order_index', models.PositiveIntegerField(null=True, blank=True)),
            ('slug', models.SlugField(unique=True)),
        ))
        db.send_create_signal('recipes', ['Category'])
        
        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(max_length=50)),
            ('summary', models.CharField(max_length=500, blank=True)),
            ('description', models.TextField(blank=True)),
            ('slug', models.SlugField(max_length=50, unique=True, null=False, blank=False)),
            ('prep_time', models.CharField(max_length=100, blank=True)),
            ('ctime', models.DateTimeField(default=datetime.datetime.now)),
            ('mtime', models.DateTimeField()),
            ('category', models.ForeignKey(orm.Category)),
            ('tags', TagField()),
        ))
        db.send_create_signal('recipes', ['Recipe'])
        
        # Adding model 'FoodGroup'
        db.create_table('recipes_foodgroup', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=150)),
        ))
        db.send_create_signal('recipes', ['FoodGroup'])
        
        # Adding model 'Direction'
        db.create_table('recipes_direction', (
            ('id', models.AutoField(primary_key=True)),
            ('text', models.TextField(blank=True)),
            ('recipe', models.ForeignKey(orm.Recipe)),
            ('order', PositionField(null=True, unique_for_field='recipe', blank=True)),
        ))
        db.send_create_signal('recipes', ['Direction'])
        
        # Adding model 'PrepMethod'
        db.create_table('recipes_prepmethod', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=60, blank=True)),
        ))
        db.send_create_signal('recipes', ['PrepMethod'])
        
        # Adding model 'Unit'
        db.create_table('recipes_unit', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=60)),
            ('name_abbrev', models.CharField(max_length=60, blank=True)),
            ('plural', models.CharField(max_length=60, blank=True)),
            ('plural_abbrev', models.CharField(max_length=60, blank=True)),
            ('type', models.IntegerField()),
        ))
        db.send_create_signal('recipes', ['Unit'])
        
        # Adding model 'Photo'
        db.create_table('recipes_photo', (
            ('id', models.AutoField(primary_key=True)),
            ('caption', models.CharField(max_length=200)),
            ('recipe', models.ForeignKey(orm.Recipe)),
            ('image', models.ImageField()),
            ('keep', models.BooleanField(default=True, editable=False)),
        ))
        db.send_create_signal('recipes', ['Photo'])
        
        # Adding model 'Food'
        db.create_table('recipes_food', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=150)),
            ('group', models.ForeignKey(orm.FoodGroup)),
        ))
        db.send_create_signal('recipes', ['Food'])
        
        # Adding model 'Ingredient'
        db.create_table('recipes_ingredient', (
            ('id', models.AutoField(primary_key=True)),
            ('amount', models.FloatField()),
            ('amountMax', models.FloatField(null=True, blank=True)),
            ('unit', models.ForeignKey(orm.Unit, null=True, blank=True)),
            ('recipe', models.ForeignKey(orm.Recipe)),
            ('food', models.ForeignKey(orm.Food)),
            ('prep_method', models.ForeignKey(orm.PrepMethod, null=True, blank=True)),
            ('order_index', PositionField(null=True, unique_for_field="direction", blank=True)),
            ('direction', models.ForeignKey(orm.Direction, null=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['Ingredient'])
        
        # Adding ManyToManyField 'Recipe.sources'
        db.create_table('recipes_recipe_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm.Recipe, null=False)),
            ('source', models.ForeignKey(orm.Source, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Source'
        db.delete_table('recipes_source')
        
        # Deleting model 'Category'
        db.delete_table('recipes_category')
        
        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')
        
        # Deleting model 'FoodGroup'
        db.delete_table('recipes_foodgroup')
        
        # Deleting model 'Direction'
        db.delete_table('recipes_direction')
        
        # Deleting model 'PrepMethod'
        db.delete_table('recipes_prepmethod')
        
        # Deleting model 'Unit'
        db.delete_table('recipes_unit')
        
        # Deleting model 'Photo'
        db.delete_table('recipes_photo')
        
        # Deleting model 'Food'
        db.delete_table('recipes_food')
        
        # Deleting model 'Ingredient'
        db.delete_table('recipes_ingredient')
        
        # Dropping ManyToManyField 'Recipe.sources'
        db.delete_table('recipes_recipe_sources')
        
    
    
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
            'ctime': ('models.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('models.TextField', [], {'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'mtime': ('models.DateTimeField', [], {}),
            'prep_time': ('models.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'False', 'blank': 'False'}),
            'sources': ('models.ManyToManyField', ["orm['recipes.Source']"], {'blank': 'True'}),
            'summary': ('models.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'tags': ('TagField', [], {}),
            'title': ('models.CharField', [], {'max_length': '50'})
        },
        'recipes.food': {
            'Meta': {'ordering': '["name","group"]'},
            'group': ('models.ForeignKey', ["orm['recipes.FoodGroup']"], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'})
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
            'order_index': ('PositionField', [], {'null': 'True', 'unique_for_field': '"direction"', 'blank': 'True'}),
            'prep_method': ('models.ForeignKey', ["orm['recipes.PrepMethod']"], {'null': 'True', 'blank': 'True'}),
            'recipe': ('models.ForeignKey', ["orm['recipes.Recipe']"], {}),
            'unit': ('models.ForeignKey', ["orm['recipes.Unit']"], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['recipes']
