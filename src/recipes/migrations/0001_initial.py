# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Source'
        db.create_table('recipes_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
        ))
        db.send_create_signal('recipes', ['Source'])

        # Adding model 'Category'
        db.create_table('recipes_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('order_index', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('recipes', ['Category'])

        # Adding model 'FoodGroup'
        db.create_table('recipes_foodgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('recipes', ['FoodGroup'])

        # Adding model 'Food'
        db.create_table('recipes_food', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('name_sorted', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.FoodGroup'])),
        ))
        db.send_create_signal('recipes', ['Food'])

        # Adding model 'PrepMethod'
        db.create_table('recipes_prepmethod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
        ))
        db.send_create_signal('recipes', ['PrepMethod'])

        # Adding model 'Photo'
        db.create_table('recipes_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('keep', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('recipes', ['Photo'])

        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('prep_time', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('ctime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('mtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Category'])),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('recipes', ['Recipe'])

        # Adding M2M table for field sources on 'Recipe'
        db.create_table('recipes_recipe_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('source', models.ForeignKey(orm['recipes.source'], null=False))
        ))
        db.create_unique('recipes_recipe_sources', ['recipe_id', 'source_id'])

        # Adding model 'Direction'
        db.create_table('recipes_direction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=-1, null=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['Direction'])

        # Adding model 'Unit'
        db.create_table('recipes_unit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name_abbrev', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('plural', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('plural_abbrev', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('recipes', ['Unit'])

        # Adding model 'Ingredient'
        db.create_table('recipes_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('amountMax', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Unit'], null=True, blank=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Food'])),
            ('prep_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.PrepMethod'], null=True, blank=True)),
            ('instruction', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('order_index', self.gf('django.db.models.fields.IntegerField')(default=-1, null=True, blank=True)),
            ('direction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Direction'], null=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['Ingredient'])


    def backwards(self, orm):
        
        # Deleting model 'Source'
        db.delete_table('recipes_source')

        # Deleting model 'Category'
        db.delete_table('recipes_category')

        # Deleting model 'FoodGroup'
        db.delete_table('recipes_foodgroup')

        # Deleting model 'Food'
        db.delete_table('recipes_food')

        # Deleting model 'PrepMethod'
        db.delete_table('recipes_prepmethod')

        # Deleting model 'Photo'
        db.delete_table('recipes_photo')

        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')

        # Removing M2M table for field sources on 'Recipe'
        db.delete_table('recipes_recipe_sources')

        # Deleting model 'Direction'
        db.delete_table('recipes_direction')

        # Deleting model 'Unit'
        db.delete_table('recipes_unit')

        # Deleting model 'Ingredient'
        db.delete_table('recipes_ingredient')


    models = {
        'recipes.category': {
            'Meta': {'ordering': "['order_index']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'order_index': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'recipes.direction': {
            'Meta': {'ordering': "['order', 'id']", 'object_name': 'Direction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'recipes.food': {
            'Meta': {'ordering': "['name_sorted']", 'object_name': 'Food'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.FoodGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name_sorted': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'})
        },
        'recipes.foodgroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'FoodGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'recipes.ingredient': {
            'Meta': {'ordering': "['direction', 'order_index', 'id']", 'object_name': 'Ingredient'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'amountMax': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Direction']", 'null': 'True', 'blank': 'True'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Food']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'order_index': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'prep_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.PrepMethod']", 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Unit']", 'null': 'True', 'blank': 'True'})
        },
        'recipes.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keep': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"})
        },
        'recipes.prepmethod': {
            'Meta': {'ordering': "['-name']", 'object_name': 'PrepMethod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        'recipes.recipe': {
            'Meta': {'ordering': "['title']", 'object_name': 'Recipe'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Category']"}),
            'ctime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'prep_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipes.Source']", 'symmetrical': 'False', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'recipes.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'})
        },
        'recipes.unit': {
            'Meta': {'ordering': "['name']", 'object_name': 'Unit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'plural': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'plural_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['recipes']
