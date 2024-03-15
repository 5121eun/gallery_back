from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.PostViewSet, basename='post')

# Wire up our API using automatic URL routin
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
]

urlpatterns += router.urls