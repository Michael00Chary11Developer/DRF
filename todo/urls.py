from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.all_todos)
]
