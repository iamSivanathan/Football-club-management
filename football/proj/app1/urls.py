from django.urls import path # type: ignore
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('home/', views.home, name='home'),

     path('standing/', views.standing, name='standing'),
     path('standadd/',views.standadd,name='standadd'),
     path('standform/<int:pk>',views.standform,name='standform'),

     path('player/', views.player, name='player'),
     path('add/',views.add,name='add'),
     path('update/<int:pk>',views.update,name='update'),
     path('remove/<int:pk>',views.remove,name='remove'),

     path('team/', views.team, name='team'),
     path('contact/', views.contact, name='contact'),

]