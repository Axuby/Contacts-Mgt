from django.contrib.auth import views as auth_view
from django.urls import re_path as url, path
from . import views


urlpatterns = [
    url(r'^password/$', views.change_password, name='change_password'),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('profile-detail/<int:pk>/',
         views.ProfileDetailView.as_view(), name="profile-detail"),
    path('forgot-password/', views.forgot_password, name="forgot-password"),
    path('reset-password-validate/<uidb64>/<token>/',
         views.reset_password_validate, name="reset-password-validate"),
    path('reset-password/', views.reset_password, name="reset-password"),
    path('edit-profile/<int:profile_pk>/',
         views.edit_profile, name="edit-profile"),
    path('change-password/', views.change_password, name="change-password"),
    path("exception/", views.page_403),
    # path('reset_password/', auth_view.PasswordResetView.as_view(),
    #      name="reset-password")

]

# urlpatterns+=[
#     path()
# ]
