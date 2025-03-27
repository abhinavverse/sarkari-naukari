from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('latest-jobs/', views.latest_jobs, name='latest_jobs'),
    path('admissions/', views.admissions, name='admissions'),
    path('results/', views.results, name='results'),
    path('admit-cards/', views.admit_cards, name='admit_cards'),
]