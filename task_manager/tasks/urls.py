from django.urls import path

from task_manager.tasks.views import (LabelFormCreateView, LabelFormDeleteView,
                                      LabelFormUpdateView, LabelIndexView,
                                      StatusFormCreateView,
                                      StatusFormDeleteView,
                                      StatusFormUpdateView, StatusIndexView)

app_name = 'tasks'

urlpatterns = [
    path("statuses/", StatusIndexView.as_view(), name='status_list'),
    path("labels/", LabelIndexView.as_view(), name='label_list'),
    path(
        'statuses/create/',
        StatusFormCreateView.as_view(),
        name='create_status'
    ),
    path(
        'statuses/<int:pk>/update/',
        StatusFormUpdateView.as_view(),
        name='update_status'
    ),
    path(
        'statuses/<int:pk>/delete/',
        StatusFormDeleteView.as_view(),
        name='delete_status'
    ),

    path('labels/create/', LabelFormCreateView.as_view(), name='create_label'),
    path(
        'labels/<int:pk>/update/',
        LabelFormUpdateView.as_view(),
        name='update_label'
    ),
    path(
        'labels/<int:pk>/delete/',
        LabelFormDeleteView.as_view(),
        name='delete_label'
    ),

]


# GET /tasks/ — страница со списком всех задач
# GET /tasks/create/ — страница создания задачи
# POST /tasks/create/ — создание новой задачи
# GET /tasks/<int:pk>/update/ — страница редактирования задачи
# POST /tasks/<int:pk>/update/ — обновление задачи
# GET /tasks/<int:pk>/delete/ — страница удаления задачи
# POST /tasks/<int:pk>/delete/ — удаление задачи
# GET /tasks/<int:pk>/ — страница просмотра задачи
