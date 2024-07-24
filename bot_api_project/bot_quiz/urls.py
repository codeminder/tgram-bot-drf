from django.urls import path
from .views import CurrentDateTimeView, RandomAdvisesView, index

urlpatterns = [
    path('', index, name='index'),
    path('api/current-datetime/', CurrentDateTimeView.as_view(), name='current-datetime'),
    path('api/random-advises/', RandomAdvisesView.as_view(), name='random-advises'),
]