"""
URL configuration for Evaluacion_1 project.

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
from django.urls import path

from app1 import views as app1
from app1 import view1_2 as app1_2
from app2 import views as app2
from app2 import view2_2 as app2_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', app1.display),
    path('app1.2/',app1_2.display),
    path('app2/', app2.display),
    path('app2.2/', app2_2.display),
]



