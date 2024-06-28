from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Nexusapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('profile/', views.profile, name='profile'),
    path('management/', views.management, name='management'),
    path('fcrime/', views.fcrime, name='fcrime'),
    path('license/', views.license, name='license'),
    path('tf/', views.tf, name='tf'),
    path('bg/', views.bg, name='bg'),
    path('slc/', views.slc, name='slc'),
    path('dlc/', views.dlc, name='dlc'),
    path('pof/', views.pof, name='pof'),
    path('facs/', views.facs, name='facs'),
    path('cfa/', views.cfa, name='cfa'),
]
