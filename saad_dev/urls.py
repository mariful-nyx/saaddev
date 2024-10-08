"""
URL configuration for saad_dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .yasg import schema_view

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('account/', include('core.urls')),
    path('dev_admin/', include('dev_admin.urls')),
    path('', include('base.urls')),
    path('saad-dev-api/', include('saad_dev_api.urls')),

    # fin app
    path('fin/', include('fin.urls')),
    path('fin_api/', include('fin_api.urls')),
    
    # todo app
    path('todo/', include('todo.urls')),

    # ecom app
    path('ecom/', include('ecom.urls')),

    # mms app
    path('mess/', include('mess_name.urls')),
    path('mms/', include('mms.urls')),

    # blog
    path('blog/', include('blog_api.urls')),
]



