from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.sign_in, name='login'),    #템플릿에서 호출할 때 name 이용
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
]
