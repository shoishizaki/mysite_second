from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<int:id>/', views.index_page, name='index_page'),
    path('templates/', views.index_template, name='index_template'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]