from django.conf import settings

def apps_installees(request):
    from django.conf import settings
    return {'apps' :  settings.INSTALLED_APPS}
