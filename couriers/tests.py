from django.test import TestCase, Client
from rest_framework.test import APIClient

from couriers.models import User, Income, IncomeDailyReport
from utils.time_utils import DateTimeUtils


# class UserTestCase(TestCase):
#     def setUp(self):
#         User.objects.create(name="ali")
#         User.objects.create(name="mohammad")
#

#
#
# class IncomeTestCase(TestCase):
#     def setUp(self):
#         user = User.objects.create(name="ali")
        # Income.objects.create(courier_id=user.id, mission_id=101, income_type_id=1, amount=100, created_at=created_at)
        # Income.objects.create(courier_id=user.id, mission_id=101, income_type_id=2, amount=-10, created_at=created_at)
        # Income.objects.create(courier_id=user.id, mission_id=101, income_type_id=2, amount=-20, created_at=created_at)
        # Income.objects.create(courier_id=user.id, mission_id=101, income_type_id=2, amount=10, created_at=created_at)

    # def test_income(self):
        # x = IncomeDailyReport.objects.all()
        # print(x)
        # user_daily_income = IncomeDailyReport.objects.get(courier_id=1)
        # self.assertEqual(user_daily_income.income, 80)
        # c = APIClient()
        # created_at = DateTimeUtils.get_time(string_format=True)
        # response = c.post('/api/couriers/1/income/', {"mission_id": 101, "income_type_id": 1, "amount": 100},
        #                   )
        # self.assertEqual(response.status_code, 200)
