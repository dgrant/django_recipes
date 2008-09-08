from recipes.models import Category

def categories(request):
    return {'categories_list': Category.objects.all()}
