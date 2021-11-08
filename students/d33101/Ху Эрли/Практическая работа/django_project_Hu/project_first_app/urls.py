from django.urls import path, re_path
from . import views
from .views import *
urlpatterns = [
    path('owner/<int:id_owner>/', views.detail),
    path('time/', views.example_view),
    path('owner_list/', views.owner_view),
    path('car/<int:pk>/', CarView.as_view()),
    path('car/list/', CarListView.as_view()),
    path('create_owner/', create_owner),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('create_car/', CarCreateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),

]