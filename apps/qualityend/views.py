from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from pickle import load


from rest_framework import viewsets
from rest_framework import mixins

from apps.qualityend.models import Endpoint
from apps.qualityend.serializers import EndpointSerializer

from apps.qualityend.models import MLAlgorithm
from apps.qualityend.serializers import MLAlgorithmSerializer

from apps.qualityend.models import MLAlgorithmStatus
from apps.qualityend.serializers import MLAlgorithmStatusSerializer

from apps.qualityend.models import MLRequest
from apps.qualityend.serializers import MLRequestSerializer



# Folgendes Segment für die Einbindung der html Seite in das Dashboard

# def quality(request):
  #   context = {'segment': 'qualityend'}

 #   html_template = loader.get_template('home/page-quality.html')
 #   return HttpResponse(html_template.render(context, request))



# Folgendes Segment von www.deploymachinelearning.com

class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()

class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()

def deactivate_other_statuses(instance):
    old_statuses = MLAlgorithmStatus.objects.filter(parent_mlalgorithm=instance.parent_mlalgorithm, created_at__lt=instance.created_at, active=True)
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    MLAlgorithmStatus.objects.bulk_update(old_statuses, ["active"])

class MLAlgorithmStatusViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithmStatus.objects.all()
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                # set active=False für other statuses
                deactivate_other_statuses(instance)

        except Exception as e:
            raise APIException(str(e))

class MLRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.UpdateModelMixin
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()
