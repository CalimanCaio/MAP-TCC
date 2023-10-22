from django.urls import path

from map.views import MethodologyListCreate, MethodologyRetrieveUpdateDestroy

urlpatterns = [
    path('methodologies/', MethodologyListCreate.as_view(), name='methodology-list'),
    path('methodologies/<int:pk>/', MethodologyRetrieveUpdateDestroy.as_view(), name='methodology-detail'),
]
