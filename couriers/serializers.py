# from django.db import transaction
from rest_framework import serializers
from couriers.models import User, Income, IncomeDailyReport, IncomeWeeklyReport


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class IncomeDailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeDailyReport
        fields = ['courier_id', 'income', 'date']


class IncomeWeeklyReportSerializer(serializers.ModelSerializer):
    courier = UserSerializer(read_only=True)

    class Meta:
        model = IncomeWeeklyReport
        fields = ['courier_id', 'income', 'date', 'courier']
