from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import refresh_jwt_token
from .users.views import UserViewSet, null_view, FacebookLogin, GoogleLogin, TwitterLogin

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # Authentication & Authorization Urls
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/rest-auth/refresh-token/', refresh_jwt_token),
    # Social accounts
    path('api/v1/rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/v1/rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/v1/rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    # The next url use /allauth/account/views.py, but we need declare a null view here
    path('api/v1/rest-auth/registration/verify-email/', null_view, name='rest_verify_email'),
    # The next url use rest_auth/views.py, but we need declare a null view here
    path('api/v1/rest-auth/password-reset/confirm/<str:uidb64>/<str:token>/', null_view,
         name='password_reset_confirm'),
    # Necessary for get error msg "User is already registered with this e-mail address."
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
