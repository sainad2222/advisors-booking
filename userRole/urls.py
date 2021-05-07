from django.urls import path
from .views import RegisterClassView,LoginClassView,ListAdvisorsView,BookAdvisorView

urlpatterns = [
    path("register/", RegisterClassView.as_view()),
    path("login/", LoginClassView.as_view()),
    path("<int:id>/advisors/", ListAdvisorsView.as_view()),
    path("<int:user_id>/advisor/<int:advisor_id>/",BookAdvisorView.as_view())
]
