"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from app.views import *
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

# We use a single global DRF Router that routes views from all apps in project
router = DefaultRouter()

# app views and viewsets
router.register(r'tool', ToolViewSet, r"tool")
router.register(r'toolversion', ToolVersionViewSet, r"toolversion")

schema_view = get_swagger_view(title='BioContainers API')

urlpatterns = [
    # default django admin interface (currently unused)
    url(r'^admin/', admin.site.urls),

    url('^$', schema_view),

    # root view of our REST api, generated by Django REST Framework's router
    url(r'^/', include((router.urls, 'api'))),

    # # index page should be served by django to set cookies, headers etc.
    # url(r'^$', index_view, {}, name='index'),
]

# # let django built-in server serve static and media content
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

