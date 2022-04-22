from datetime import timedelta

from django.db import transaction
from django.db.models.utils import resolve_callables

from couriers.models import User, Income, IncomeDailyReport, IncomeWeeklyReport
from couriers.serializers import UserSerializer, IncomeSerializer, IncomeDailyReportSerializer, \
    IncomeWeeklyReportSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from utils.time_utils import DateTimeUtils


class CourierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Couriers to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path="(?P<courier_id>[0-9]+)/income")
    def get_courier_income(self, request, courier_id=None):
        queryset = Income.objects.all()
        serializer = IncomeSerializer(queryset.filter(courier_id=courier_id), many=True)
        return Response(serializer.data)

    @get_courier_income.mapping.post
    @transaction.atomic
    def add_courier_income(self, request, courier_id=None):
        sid = transaction.savepoint()
        data = request.data
        created_at = DateTimeUtils.get_time(string_format=True)
        data.update({
            "courier": courier_id,
            "created_at": created_at
        })
        # print(data, type(courier_id))
        serializer = IncomeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # print("ldsjfkldsjflsjf", serializer.validated_data, serializer.validated_data["courier"].id)
        date = DateTimeUtils.string_to_datetime(created_at).date()
        data = {
            "courier_id": serializer.validated_data["courier"].id,
            "date": date,
            "income": serializer.validated_data["amount"]
        }

        income_report_serializer = IncomeDailyReportSerializer(data=data)
        income_report_serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            self.update_daily_report(data, date, courier_id)
            self.update_weekly_report(data, date, courier_id)

            transaction.savepoint_commit(sid)
            return Response(serializer.data)

        except Exception as e:
            transaction.savepoint_rollback(sid)
            return Response({"success": False, "error": str(e) if str(e) else "unknown error!"})

    def update_daily_report(self, data, date, courier_id):
        obj, created = IncomeDailyReport.objects.select_for_update().get_or_create(data, courier_id=courier_id,
                                                                                   date=date)
        if not created:
            for k, v in resolve_callables(data):
                if k == "income":
                    setattr(obj, k, v + obj.income)
                    continue
                setattr(obj, k, v)
            obj.save(using=IncomeDailyReport.objects.db)

    def update_weekly_report(self, data, date, courier_id):
        start_date_of_week = date - timedelta(days=date.weekday() + 2)
        data["date"] = start_date_of_week

        income_report_serializer = IncomeWeeklyReportSerializer(data=data)
        income_report_serializer.is_valid(raise_exception=True)

        obj, created = IncomeWeeklyReport.objects.select_for_update().get_or_create(data, courier_id=courier_id,
                                                                                    date=start_date_of_week)
        if not created:
            for k, v in resolve_callables(data):
                if k == "income":
                    setattr(obj, k, v + obj.income)
                    continue
                setattr(obj, k, v)
            obj.save(using=IncomeWeeklyReport.objects.db)


class IncomeWeeklyReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Income Report to be viewed or edited.
    """
    queryset = IncomeWeeklyReport.objects.all()
    serializer_class = IncomeWeeklyReportSerializer

    def list(self, request, *args, **kwargs):
        try:
            from_date = request.query_params.get('from_date')
            to_date = request.query_params.get('to_date')
            from_date = DateTimeUtils.string_to_date(from_date).date()
            to_date = DateTimeUtils.string_to_date(to_date).date()
        except:
            return Response({"error": "time format is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        if from_date > to_date:
            return Response({"to_date": "to_date must be greater than from_date"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = IncomeWeeklyReportSerializer(self.queryset.filter(date__range=[from_date, to_date]),
                                                  many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            from_date = request.query_params.get('from_date')
            to_date = request.query_params.get('to_date')
            from_date = DateTimeUtils.string_to_date(from_date).date()
            to_date = DateTimeUtils.string_to_date(to_date).date()
        except:
            return Response({"error": "time format is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        if from_date > to_date:
            return Response({"to_date": "to_date must be greater than from_date"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = IncomeWeeklyReportSerializer(self.queryset.filter(courier_id=pk, date__range=[from_date, to_date]),
                                                  many=True)
        return Response(serializer.data)


class IncomeDailyReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Income Report to be viewed or edited.
    """
    queryset = IncomeDailyReport.objects.all()
    serializer_class = IncomeDailyReportSerializer

    def list(self, request, *args, **kwargs):
        serializer = IncomeDailyReportSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer = IncomeDailyReportSerializer(self.queryset.filter(courier_id=pk), many=True)
        return Response(serializer.data)
