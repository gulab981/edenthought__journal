from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name=''),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.log_out,name='logout'),
    path('create-thought',views.create_thought,name='create-thought'),
    path('my-thoughts',views.my_thoughts,name='my-thoughts'),
    path('update-thought/<str:pk>',views.update_thought,name='update-thought'),
    path('delete-thought/<str:pk>',views.delete_thought,name='delete-thought'),
    path('profile',views.profile,name='profile'),
    path('delete-account',views.delete_account,name='delete-account'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='journal/password-reset.html'),name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='journal/password-reset-sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='journal/password-reset-form.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='journal/password-reset-complete.html'),name='password_reset_complete'),
]
