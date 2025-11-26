from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register_user,name='register_user'),
    path('create/post/', views.create_post,name='create_post'),
    path('all/post/', views.all_post,name='all_post'),
    path('update/post/<int:pk>/', views.update_post,name='update_post'),
    path('delete/post/<int:pk>/', views.delete_post,name='delete_post'),
    path('update/user/profile/', views.update_user_profile,name='update_user'),
]
