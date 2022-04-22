from __future__ import absolute_import
from celery import Celery
from django.db.models.utils import resolve_callables
from couriers.models import IncomeDailyReport
from couriers.serializers import IncomeWeeklyReportSerializer
from datetime import timedelta
import os
from django.conf import settings


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miare.settings')

app = Celery('miare')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
# celery -A tasks worker --loglevel=INFO
@app.task
def add(x, y):
    return x + y

#
# @app.task
# def weekly_income_process(data):
#     # end = start + timedelta(days=6)
#
#     start_date_of_week = date - timedelta(days=date.weekday() + 2)
#     data["date"] = start_date_of_week
#
#     income_report_serializer = IncomeWeeklyReportSerializer(data=data)
#     income_report_serializer.is_valid(raise_exception=True)
#
#     obj, created = IncomeWeeklyReport.objects.select_for_update().get_or_create(data, courier_id=courier_id,
#                                                                                 date=start_date_of_week)
#     if not created:
#         for k, v in resolve_callables(data):
#             if k == "income":
#                 setattr(obj, k, v + obj.income)
#                 continue
#             setattr(obj, k, v)
#         obj.save(using=IncomeWeeklyReport.objects.db)
