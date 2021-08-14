from django.urls import path

from . import views

app_name = 'honameuro'

urlpatterns = [
    path('', views.main, name='main'),
    path('individual/', views.indiv, name='indiv'),
    path('individual/topic/<int:topic_id>', views.indiv_topic, name='indiv_topic'),
    path('individual/topic/<int:indiv_id>/', views.indiv_detail, name='indiv_detail'),
    path('individual/indiv_local/', views.indiv_local, name='indiv_local'),
    path('individual/create', views.indiv_create, name='indiv_create'),
    path('individual/submit', views.indiv_submit, name='indiv_submit'),
    path('local/', views.local, name='local'),
    path('local/detail/', views.local_detail, name='local_detail'),
    path('local/match/', views.local_match, name='local_match'),
    path('local/match/<int:indiv_id>/', views.match_detail, name='match_detail'),
    path('apply/<int:village_id>/', views.apply, name='apply'),
]
