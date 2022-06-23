from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path('<int:poke_id>',views.index),
]
