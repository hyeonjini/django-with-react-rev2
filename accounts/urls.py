from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # /accounts/login/ => setting.LOGIN_URL
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('signup/', views.signup, name="signup"),
    path('edit/', views.profile_edit, name="profile_edit"),

    re_path(r'^(?P<username>[\w.@+-]+)/follow/$', views.user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/unfollow/$', views.user_unfollow, name='user_unfollow'),

]
