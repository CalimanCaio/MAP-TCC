from django.urls import path

from map.views import MethodologyListCreate, MethodologyRetrieveUpdateDestroy, ActivityListCreate, \
    ActivityRetrieveUpdateDestroy

urlpatterns = [
    path('methodologies/', MethodologyListCreate.as_view(), name='methodology-list'),
    path('methodologies/<int:pk>/', MethodologyRetrieveUpdateDestroy.as_view(), name='methodology-detail'),

    path('activities/', ActivityListCreate.as_view(), name='activity-list'),
    path('activities/<int:pk>/', ActivityRetrieveUpdateDestroy.as_view(), name='activity-detail'),
]
