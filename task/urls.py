from django.urls import path

from .views import TaskDetail, TaskList

app_name="task"

urlpatterns = [
    path("", TaskList.as_view(),  ),
    path("<int:pk>/", TaskDetail.as_view(),  ),
]