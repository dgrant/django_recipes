from django.contrib import admin
from django.forms.models import inlineformset_factory
from .models import *

class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_index')
    prepopulated_fields = {'slug': ('name',)}

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_sorted', 'name', 'group', 'conversion_src_unit', 'conversion_factor',)
    list_filter = ('group',)
    search_fields = ('name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'conversion_src_unit':
            kwargs["queryset"] = Unit.objects.exclude(type=Unit.TYPE.mass)
        return super(FoodAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class PhotoInlineAdmin(admin.StackedInline):
    model = Photo
    extra = 2

class DirectionInlineAdmin(admin.TabularInline):
    model = Direction
    extra = 3

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_abbrev', 'plural_abbrev', 'system', 'type',)

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('food', 'unit', 'amount', 'prep_method', 'direction',)

class IngredientInlineAdmin(admin.TabularInline):
    model = Ingredient
    extra = 6

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "direction":
            recipe = self.get_object(request, Recipe)
            kwargs["queryset"] = Direction.objects.filter(recipe=recipe)
        return super(IngredientInlineAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_object(self, request, model):
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-1]
        try:
            object_id = int(object_id)
        except ValueError:
            return None
        return model.objects.get(pk=object_id)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'slug', 'prep_time',)
    fields = ('title', 'slug', 'category', 'summary', 'description', 'serving_value', 'serving_string', 'sources', 'prep_time',)
    list_filter = ('title', 'sources',)
    search_fields = ('title', 'description', 'summary',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    model = Recipe
    inlines = [DirectionInlineAdmin, IngredientInlineAdmin, PhotoInlineAdmin]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            kwargs["queryset"] = Category.objects.all().order_by('name')
        return super(RecipeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class ServingStringAdmin(admin.ModelAdmin):
    model = ServingString

admin.site.register(Source, SourceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodGroup)
admin.site.register(Food, FoodAdmin)
admin.site.register(PrepMethod)
admin.site.register(Photo)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(ServingString, ServingStringAdmin)
