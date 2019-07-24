
from django.urls import path
from . import views
urlpatterns = [

    path('',views.show_weather ),
    path('<id>/del',views.delete,name='del_view'),
]