from django.urls import path
from .views import AdvisorViewClass

urlpatterns = [
        path('advisor/',AdvisorViewClass.as_view()),
        ]

