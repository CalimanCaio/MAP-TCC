from django.urls import path

from map.views import MethodologyListCreate, MethodologyRetrieveUpdateDestroy, ActivityListCreate, \
    ActivityRetrieveUpdateDestroy, ProjectListCreate, ProjectRetrieveUpdateDestroy

urlpatterns = [
    path('methodologies/', MethodologyListCreate.as_view(), name='methodology-list'),
    path('methodologies/<int:pk>/', MethodologyRetrieveUpdateDestroy.as_view(), name='methodology-detail'),

    path('activities/', ActivityListCreate.as_view(), name='activity-list'),
    path('activities/<int:pk>/', ActivityRetrieveUpdateDestroy.as_view(), name='activity-detail'),

    path('projects/', ProjectListCreate.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),
]
