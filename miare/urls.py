from django.urls import include, path
from rest_framework import routers
from couriers import views as courier_views


# router = routers.DefaultRouter()
# router.register('', courier_views.CourierViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include('couriers.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
