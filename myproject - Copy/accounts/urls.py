from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.registration_view, name='register'),
    path('enrollment_data/', views.enrollment_data, name='enrollment_data'),
    path('add_face/', views.add_face, name='add_face'),
]