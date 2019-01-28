from django.contrib import admin

from .models import Category, Direction, Food, FoodGroup, Ingredient, Photo, PrepMethod, Recipe, ServingString,\
    Source, Unit

from .admin_mixins import CachedChoiceFieldOptionsMixin


class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_index')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


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


class IngredientInlineAdmin(CachedChoiceFieldOptionsMixin, admin.TabularInline):
    model = Ingredient
    extra = 6
    cached_choice_fields = ['prep_method', 'unit', 'food', 'direction',]

    def get_filters(self, obj):
        return (('direction', dict(recipe=obj),),)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        """
        Only allow choosing directions from the directions that are in this recipe
        """
        field = super(IngredientInlineAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'direction':
            if request._obj_:
                field.queryset = field.queryset.filter(recipe=request._obj_)  
            else:
                field.queryset = field.queryset.none()

        return field


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'slug', 'prep_time',)
    fields = (
        'title', 'slug', 'category', 'summary', 'description', 'serving_value', 'serving_string', 'sources',
        'prep_time',)
    list_filter = ('title', 'sources',)
    search_fields = ('title', 'description', 'summary',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    model = Recipe
    inlines = [DirectionInlineAdmin, IngredientInlineAdmin, PhotoInlineAdmin]

    def get_form(self, request, obj=None, **kwargs):
        """
		just save obj reference for future processing in Inline
		"""
        request._obj_ = obj
        return super(RecipeAdmin, self).get_form(request, obj, **kwargs)


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
