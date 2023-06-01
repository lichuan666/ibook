from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

    path('admin/', include('admin.urls')),
    path('log/', include('login.urls')),
    path('index/', include('index.urls')),

    path('schedule', include('schedule.urls'))

]
