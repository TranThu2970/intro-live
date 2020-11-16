from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('team/',views.team, name='team'),
    path('project/',views.project, name='project'),
    path('field/',views.field, name='field'),
    path('detail/<slug:slug>',views.fieldDetail, name='detail'),
    path('contact/',views.contact, name='contact')
]