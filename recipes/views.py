from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from models import Recipe, Direction, Ingredient

from django.views.generic import ListView, CreateView, DetailView


def root(request):
    return HttpResponseRedirect("/cookbook")

class RecipeListView(ListView):
    model = Recipe
    paginate_by = 25

    def get_queryset(self):
        qs = Recipe.objects.all()
        return qs

class RecipeDetailView(DetailView):
    model = Recipe
