
from django.urls import path
from .views import RegisterClassView,LoginClassView

urlpatterns = [
    path("register/", RegisterClassView.as_view()),
    path("login/", LoginClassView.as_view()),
]
