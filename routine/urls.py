from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('base/',views.base,name='base'),
    # path('base2/',views.base2,name='base2'),
    path('haxi/',views.haxi,name='haxi'),
    path('jsys/',views.jsys,name='jsys'),
    path('jsys2/',views.jsys2,name='jsys2'),
    path('bmi/',views.bmi,name='bmi'),
    path('weather/',views.weather,name='weather'),
]