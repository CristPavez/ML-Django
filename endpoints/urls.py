# backend/server/apps/endpoints/urls.py file

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from  endpoints.views import EndpointViewSet
from  endpoints.views import MLAlgorithmViewSet
from  endpoints.views import MLAlgorithmStatusViewSet
from  endpoints.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path(r"", include(router.urls)),
]
#^api/v1/