"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('a/',views.about,name="about"),
    path('c/',views.contact,name="contact"),
    path('s/',views.Signup,name="signup"),
    path('l/',views.Login,name="login"),
    path('lo/',views.Logout,name="logout"),
    path('d/',views.Dash,name='dashboard'),
    path('profile/',views.Profile,name="profile"),
    path('pass/',views.changepass,name='changepass'),
    path('add/',views.Add,name='add'),
    path('edit/<int:id>/',views.Edit,name='edit'),
    path('delete/<int:id>/',views.Delete,name='delete'),
    path('detail/<int:id>/',views.Detail,name='detail'),
]
