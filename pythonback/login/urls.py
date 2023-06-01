from django.urls import path

from . import views

# app_name = 'login'
urlpatterns = [
    path('', views.login, name="index"),  #
    path('login/', views.login, name="login"),  #
    path('register/', views.register, name="register"),  #
    path('pwd_update/', views.password_update, name="pwd_update"),  # 修改密码
    path('logout/', views.logout, name="logout"),  # 退出登录
]
