from recipes.models import Category, Recipe

# put a list of categories into the template
def categories(request):
    return {'categories_list': Category.objects.all()}

def new_recipes(request):
    return {'recipes_new_list': Recipe.objects.order_by("-ctime")}

def changed_recipes(request):
    return {'recipes_changed_list': Recipe.objects.order_by("-mtime")}
