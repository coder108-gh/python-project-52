from task_manager import views

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path('login/', views.TaskManagerLoginView.as_view(), name='login'),
    path('logout/', views.TaskManagerLogoutView.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]
