from django.urls import path, re_path, include
from apps.qualityend import views
from rest_framework.routers import DefaultRouter

from apps.qualityend.views import EndpointViewSet
from apps.qualityend.views import MLAlgorithmViewSet
from apps.qualityend.views import MLAlgorithmStatusViewSet
from apps.qualityend.views import MLRequestViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'qualityend/', EndpointViewSet, basename='endpointViewSet')
router.register(r'mlalgorithms/', MLAlgorithmViewSet, basename= 'mlalgorithms')
router.register(r'mlalgorithmstatuses/', MLAlgorithmStatusViewSet, basename='mlalgorithmstatuses')
router.register(r'mlrequests/', MLRequestViewSet, basename='mlrequests')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]




# urlpatterns = [
  #  path('qualityend', views.quality, name='qualityend'),   #  das hier für "normales" Dashboard
# ]
