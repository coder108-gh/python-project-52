from task_manager import views  
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.IndexView.as_view()),
    path('admin/', admin.site.urls),
]