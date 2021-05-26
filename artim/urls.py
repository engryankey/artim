from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage, redirect_to_home, UserDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.html',
            subject_template_name='password_reset_subject.txt',
            email_template_name='password_reset_email.html'
            ),
        name='password_reset',
    ),
    path(
        'password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path('<slug>/', HomePage.as_view(), name='index'),
    path('account/', include('accounts.urls')),
    path('', redirect_to_home),
    path('<str:user_type>/<slug:slug>/', UserDetailView.as_view(), name='user-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)