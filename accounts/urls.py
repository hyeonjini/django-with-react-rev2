from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), # /accounts/login/ => setting.LOGIN_URL
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('signup/', views.signup, name="signup"),
    path('edit/', views.profile_edit, name="profile_edit"),

]