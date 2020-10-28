from django.conf.urls import include, url

import YaraGuardian.API.urls

from django.contrib import admin
from django.contrib.auth import views as auth_views
from YaraGuardian.views import Index, Login, Logout, RecoverPassword, RegisterAccount, Healthz


urlpatterns = [url(r'^$',
                   Index.as_view(),
                   name='Index'),

               url(r'^healthz$',
                   Healthz.as_view(),
                   name='Healthz'),

               url(r'^API/',
                   include(YaraGuardian.API.urls)),

               url(r'^admin/',
                   admin.site.urls),

               url(r'^login/$',
                   Login.as_view(),
                   name='Login'),

               url(r'^register/$',
                   RegisterAccount.as_view(),
                   name='RegisterAccount'),

               url(r'^recover/$',
                   RecoverPassword.as_view(),
                   name='RecoverPassword'),

               url(r'^logout/$',
                   Logout.as_view(),
                   name='Logout'),

               url(r'^social/',
                   include('social_django.urls',
                   namespace='social')),

               url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
                   auth_views.PasswordResetConfirmView.as_view(), {'template_name': 'prelogin/ResetPassword.html'},
                   name='password_reset_confirm'),

               url(r'^reset/done/$',
                   auth_views.PasswordResetCompleteView.as_view(), {'template_name': 'prelogin/ResetPasswordSuccess.html'},
                   name='password_reset_complete'),

]
