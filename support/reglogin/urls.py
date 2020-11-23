from django.contrib import admin
from django.urls import path
from reglogin.views import login,register,activate_account
from django.conf.urls import url

 
urlpatterns = [
    path('login' ,login),
    path('signup' ,register),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate_account),
    # path('<str:uid>&<str:token>',activate_account)
]
  