"""
URL configuration for calculator project.

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

from operation.views import AdditionView
from operation.views import SubtractionView
from operation.views import BmiView
from operation.views import VehicleAddView
from operation.views import BmrView
from operation.views import MilegeView
from operation.views import CalorieView
from operation.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition/',AdditionView.as_view(),name="add"),
    path('sub/',SubtractionView.as_view(),name="sub"),
    path('bmi/',BmiView.as_view(),name="bmi"),
    path('vehicle/',VehicleAddView.as_view(),name="vehicle"),
    path('bmr/',BmrView.as_view(),name="bmr"),
    path('milage/',MilegeView.as_view(),name="milege"),
    path('calorie/',CalorieView.as_view(),name="calorie"),
    path('',IndexView.as_view(),name="index"),

]
