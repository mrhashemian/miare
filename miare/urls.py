from django.urls import include, path

urlpatterns = [
    path('api/', include('couriers.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
