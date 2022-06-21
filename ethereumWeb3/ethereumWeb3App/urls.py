from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name="home"),
    path('login/', views.loginPage, name="login"),
    path('Signup/', views.registerPage, name="Signup"),
    path('userView/<str:userkey>', views.userView, name="userView"),
    path('blog/', views.blog, name="blog"),
    path('logout/', views.logoutUser, name="logout"),
    path('UploadFile/', views.Upload, name="UploadFile"),
    path('ViewAssets/', views.history, name="history")
]