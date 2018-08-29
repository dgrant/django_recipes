from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import Recipe, Food


def root(request):
    return HttpResponseRedirect("/cookbook")


class RecipeListView(ListView):
    model = Recipe
    paginate_by = 100

    def get_queryset(self):
        qs = Recipe.objects.all()
        return qs


class RecipeDetailView(DetailView):
    model = Recipe

    def get_object(self, queryset=None):
        recipe = super(RecipeDetailView, self).get_object(queryset=queryset)
        if 'scale' in self.request.GET:
            recipe.scale = float(self.request.GET['scale'])
            print("set scale to", recipe.scale)
        else:
            recipe.scale = 1.0
        return recipe


class FoodConversionListView(ListView):
    model = Food

    def get_queryset(self):
        qs = Food.objects.with_conversions()
        return qs
