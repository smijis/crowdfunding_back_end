from django.urls import path
from . import views # . means in this current directory - import the views file

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()), #<int:pk> means there will be an integar there, save it as a primary key
]