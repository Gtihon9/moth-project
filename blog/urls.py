from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.default, name='default'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>', views.getuserprofile, name='getuserprofile'),
]
