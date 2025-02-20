from django.urls import path
from .views import UserListView, UserDetailView, ProjectListView, ProjectDetailView, NewsListView, NewsDetailView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('project/<int:pk>/', ProjectDetailView.as_view()),
    path('newss/', NewsListView.as_view()),
    path('news/<int:pk>/', NewsDetailView.as_view()),
 ]