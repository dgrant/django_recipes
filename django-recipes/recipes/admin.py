from django.contrib import admin
from models import *

class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_index')
    prepopulated_fields = {'slug': ('name',)}

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group',)
    search_fields = ('name',)

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2

class DirectionInline(admin.TabularInline):
    model = Direction
    extra = 3

class UnitAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'plural', 'name_abbrev', 'plural_abbrev' )

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 6

    def formfield_for_dbfield(self, db_field, instance=None, **kwargs):
        """
        Modified to accept an instance parameter
        """
        #modify queryset for field named direction
        if db_field.name == "direction" and instance is not None:
            kwargs['queryset'] = Direction.objects.filter(recipe = instance.id)
            return db_field.formfield(**kwargs) # Get the default field
        elif db_field.name == "direction" and instance is None:
            kwargs['queryset'] = Direction.objects.filter(recipe = 2394324)
            return db_field.formfield(**kwargs) # Get the default field
        else:
            return super(IngredientInline, self).formfield_for_dbfield(db_field, **kwargs)

    def get_formset(self, request, obj=None):
        """Returns a BaseInlineFormSet class for use in admin add/change views."""
        if self.declared_fieldsets:
            fields = flatten_fieldsets(self.declared_fieldsets)
        else:
            fields = None
        return inlineformset_factory(self.parent_model, self.model,
            form=self.form, formset=self.formset, fk_name=self.fk_name,
            fields=fields,
            formfield_callback=lambda db_field, **kwargs:self.formfield_for_dbfield(db_field, instance=obj, **kwargs),
            extra=self.extra, max_num=self.max_num)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'summary', 'slug', 'prep_time', )
    fields = ( 'title', 'slug', 'category', 'summary', 'description', 'sources',
            'prep_time', 'tags', )
    list_filter = ( 'title', 'sources', )
    search_fields = ( 'title', 'description', 'summary', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    model = Recipe
    inlines = [DirectionInline, IngredientInline, PhotoInline]


admin.site.register(Source, SourceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodGroup)
admin.site.register(Food, FoodAdmin)
admin.site.register(PrepMethod)
admin.site.register(Photo)
admin.site.register(Recipe, RecipeAdmin)
#admin.site.register(Direction)
admin.site.register(Unit, UnitAdmin)
#admin.site.register(Ingredient, IngredientAdmin)
