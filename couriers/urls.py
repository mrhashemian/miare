from django.urls import include, path
from rest_framework import routers
from couriers import views

router = routers.DefaultRouter()
router.register(r'couriers', views.CourierViewSet)
router.register(r'reports/daily/couriers', views.IncomeDailyReportViewSet)
router.register(r'reports/weekly/couriers', views.IncomeWeeklyReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
