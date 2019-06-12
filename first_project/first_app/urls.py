from django.urls import path
from first_app import views

# template tagging
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('logout/', views.user_logout, name = 'logout'), 
    path('special/', views.special, name = 'special'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('register/', views.register, name = 'register'),
    path('relative/', views.relative, name = 'relative'),
    path('other/', views.other, name = 'other'),
    path('formpage/', views.form_name_view, name = 'formpage'),
    path('userdetails/', views.user_details, name = 'user_details'),
]
