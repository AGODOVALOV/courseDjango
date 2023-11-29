from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:course_id>', views.single_course)
]
