from django.urls import path
from .views import HomePageView

urlpatterns = [
    # path("", views.AuthView.as_view(), name="authIndex"),
    path('', HomePageView.as_view(), name='home'),
]