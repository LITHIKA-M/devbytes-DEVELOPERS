from django.contrib import admin
from django.urls import path 

from authentication import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
  path('', views.home,name="home"),
  path('signup', views.signup, name="signup"),

  # path('signin', views.signin, name="signin"),
  # path('sign_up', views.signup, name="signup"),
  # path('signout', views.signout, name="signout"),

]

urlpatterns += staticfiles_urlpatterns()

