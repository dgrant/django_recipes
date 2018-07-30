import django

def django_version(_):
    return {
        'django_version': '.'.join([str(x) for x in django.VERSION])
        }
