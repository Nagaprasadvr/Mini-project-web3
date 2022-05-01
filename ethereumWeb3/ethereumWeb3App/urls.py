from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name="home"),
    path('login/', views.loginPage, name="login"),
    path('Signup/', views.registerPage, name="Signup"),
    path('blog/', views.blog, name="blog"),
    path('logout/', views.logoutUser, name="logout"),
]