from rest_framework import routers

from marketplace.views import ExecutorView

# router = routers.DefaultRouter()
# router.register(r'executor', ExecutorViewSet)

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('v1/executor/', ExecutorView.as_view()),
    path('v1/executor/<int:pk>', ExecutorView.as_view())

]
