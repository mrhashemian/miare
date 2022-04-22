# from django.db import transaction
from rest_framework import serializers
from couriers.models import User, Income, IncomeDailyReport, IncomeWeeklyReport
from utils.time_utils import DateTimeUtils


class UserSerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name']


class IncomeSerializer(serializers.ModelSerializer):
    # courier_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Income
        fields = '__all__'
        # exclude = ['courier']

    # @transaction.atomic
    # def save_income(self, created_at):
    #     self.save()
    #     date = DateTimeUtils.string_to_date(created_at).date()
    #     data = {
    #         "courier_id": self.data["courier_id"],
    #         "date": date,
    #         "income": self.data["amount"]
    #     }
    #     print(data)
    #     income_report_serializer = IncomeReportSerializer(data=data)
    #     income_report_serializer.is_valid(raise_exception=True)
    #
    #     income_report_serializer.save()


class IncomeDailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeDailyReport
        fields = ['courier_id', 'income', 'date']


class IncomeWeeklyReportSerializer(serializers.ModelSerializer):
    courier = UserSerializer(read_only=True)

    # courier = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)

    class Meta:
        model = IncomeWeeklyReport
        fields = ['courier_id', 'income', 'date', 'courier']
