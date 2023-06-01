'''
#改了试试
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('student/', views.student.Index, name="Bookings"),  # 选择预约自习室
]


'''

#原版
from django.urls import path, re_path

from . import views        #from . 

urlpatterns = [
    path('room/', views.stu_room_available, name="Bookings"),  # 选择预约自习室
    path('seat/', views.seat, name="seat"),  # 预约座位
    path('reservation/', views.exe_reservation, name="recording"),  # 预约座位
    path('view_reservation/', views.view_reservation, name="view_reservation"),  # 查看预约记录
    path('warn/', views.view_my_warn, name="warn"),  # 警告记录
    path('sign/', views.sign, name="sign"),  # 签到
    path('recommend/', views.recommend, name="recommend"),  # 推荐
]
