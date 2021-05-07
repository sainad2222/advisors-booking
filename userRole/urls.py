from django.urls import path
from .views import RegisterClassView,LoginClassView,ListAdvisorsView

urlpatterns = [
    path("register/", RegisterClassView.as_view()),
    path("login/", LoginClassView.as_view()),
    path("<int:id>/advisors/", ListAdvisorsView.as_view()),
]
