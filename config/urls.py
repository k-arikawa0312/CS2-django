"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
import blog.views
import forecast.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('hello/',blog.views.hello,name='hello'),
    path('redirect/',blog.views.redirect_test,name='redirect_test'),
    path('<int:article_id>/',blog.views.detail,name='detail'),
    path('<int:article_id>/update/',blog.views.update,name='update'),
    path('<int:article_id>/delete/',blog.views.delete,name='delete'),
]