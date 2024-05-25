from django.contrib import admin
from django.urls import path
from modelformapp.views import Home,RegInput,RegInsert,LoginInput,LoginVerf
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view()),
    path('reginput/',RegInput.as_view()),
path('reginput/reg/',RegInsert.as_view()),
    path('logininput/',LoginInput.as_view()),
path('logininput/login/',LoginVerf.as_view()),
]