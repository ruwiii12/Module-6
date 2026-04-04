from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('basic_list/<int:pk>/', views.basic_list, name='basic_list'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('change_password/<int:pk>/', views.change_password, name='change_password'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),
    path('better_menu/<int:pk>/', views.better_menu, name='better_menu'),
    path('logout/', views.logout, name='logout'),
    path('add_menu/<int:pk>/', views.add_menu, name='add_menu'),
    path('view_detail/<int:upk>/<int:dpk>/', views.view_detail, name='view_detail'),
    path('delete_dish/<int:upk>/<int:dpk>/', views.delete_dish, name='delete_dish'),
    path('update_dish/<int:upk>/<int:dpk>/', views.update_dish, name='update_dish'),
]