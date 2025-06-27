from django.urls import path
from . import views

urlpatterns = [
    path('webhook/online/', views.online_webhook),
    path('webhook/offline/', views.offline_webhook),
    path('webhook/yoga/', views.yoga_webhook),
]
