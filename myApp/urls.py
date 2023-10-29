from django.urls import path
from . import  views


urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('item/insert/',views.insert,name='insert'),
    path('item/<int:pk>/update/', views.update, name='update'),
    path('item/<int:pk>/delete/', views.delete, name='delete'),
]

