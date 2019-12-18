"""k_working URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import create_task, TaskViewSet, \
    create_collected_data, get_analysis, get_result

router = routers.DefaultRouter()
router.register(r'entities', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/analysis/', create_task),
    path('api/result/<task_id>', get_result),
    path('api/private/analized_data/', get_analysis),
    path('api/private/parsing_result/', create_collected_data),

    path('api/', include(router.urls)),

    # path('api/analysis', include(router))
    # path('api/analysis', include('rest_framework.urls', namespace='rest_framework'))
]
