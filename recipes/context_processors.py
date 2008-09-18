from recipes.models import Category

# put a list of categories into the template
def categories(request):
    return {'categories_list': Category.objects.all()}
