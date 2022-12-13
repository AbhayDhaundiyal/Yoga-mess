from django.urls import URLPattern
from . import views
from django.urls import path

app_name = 'dash'

urlpatterns =[
    path('userSignup/', views.signup, name='create_user'),
    path('userLogin/', views.login, name='login'),
    path('userUpdate/', views.update, name='update'),
]