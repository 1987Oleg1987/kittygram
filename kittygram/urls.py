from django.urls import path

from cats.views import CatViewSet

urlpatterns = [
    path('cats/', CatViewSet.as_view({'get': 'list', 'post': 'create'})),
    path(
        'cats/<int:pk>/',
        CatViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            }
        ),
    ),
]
