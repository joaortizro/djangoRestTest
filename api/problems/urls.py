from django.urls import path
from .views import ProblemList

problem_urlpatterns = [
    path('', ProblemList.as_view())
]
