from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path
from boards import views
from account import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page_view, name='index-page'),
    path('boards/<int:pk>/', views.board_details_view, name='board-details'),
    path('boards/<int:pk>/new/', views.new_topic_view, name='new_topic'),
    path('boards/<int:board_pk>/topics/<int:topic_pk>/', views.topic_posts, name="topic_posts"),
    path('signup/', auth_views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('reset_password/', PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html', subject_template_name='password_reset_subject.txt'), name="reset_password"),
    path('reset_password/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_comlete.html'), name='reset_password_complete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)