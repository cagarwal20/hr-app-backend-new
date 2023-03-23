"""mysite URL Configuration

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
from django.urls import path,include
from staff import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_staff/',views.get_staff),
    path('get_profile/<int:id>/',views.get_profile),
    path('intime/<int:id>/',views.intime),
    path('outtime/<int:id>/',views.outtime),
    path('login/',views.login),
    path('register/',views.register),
    path('update_staff/<int:id>/',views.edit_info),
    path('delete_staff/',views.delete_staff),
    path('create_staff/',views.create_staff),
    path('fetch_attendance/<int:id>/',views.get_attendance),
    path('get_list_delete/',views.get_list_delete),
    path('get_money/',views.get_single_record),
    path('add_settle_money/<int:id>/',views.settle_money),
    path('add_money_log/<int:id>/',views.moneylog),
    path('get_money_logs/' , views.get_money_logs),
]
