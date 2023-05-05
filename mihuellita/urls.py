"""mihuellita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from registro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('registrar/', views.registrar, name="registrar"),
    path('acerca/', views.acerca, name="acerca"),
    path('consejos/', views.consejos, name="consejos"),
    path('estadisticas/', views.estadisticas, name="estadisticas"),
    path('articulo1/', views.articulo1, name="articulo1"),
    path('articulo2/', views.articulo2, name="articulo2"),
    path('articulo3/', views.articulo3, name="articulo3"),
    path('articulo_chable/', views.art_chable, name="articulo_chable"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)