#new file from v1.0.5 release

from django.conf import settings

def cfg_assets_root(request):

    return { 'ASSETS_ROOT' : settings.ASSETS_ROOT }
