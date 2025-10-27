from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    # custom audience registration view
    path('auth/register-audience', views.AudienceRegistrationView.as_view(), name='register-audience')

    # router urls for ModelViewSets
    path('', include(router.urls))
]