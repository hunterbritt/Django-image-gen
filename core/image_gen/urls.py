from . import views
from django.urls import path

# rest_framwork imports
from rest_framework.routers import DefaultRouter


# Set app_name
app_name = "image_gen"

router = DefaultRouter()

# register views via router
router.register(r"generate", views.GenerateImage, basename="generate_image")

urlpatterns = [
    path('test/', views.test, name='test_hd_generations')
]


urlpatterns += (router.urls)