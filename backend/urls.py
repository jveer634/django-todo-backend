from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path("task/", include("task.urls", namespace="task")),
    path("api/", include("rest_framework.urls"))
]