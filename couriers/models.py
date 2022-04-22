from django.db import models


class User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Income(models.Model):
    courier = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    mission_id = models.IntegerField()
    income_type_id = models.IntegerField()
    amount = models.IntegerField()
    created_at = models.DateTimeField()


class IncomeDailyReport(models.Model):
    courier = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    income = models.IntegerField()
    date = models.DateField()


class IncomeWeeklyReport(models.Model):
    courier = models.ForeignKey(User, default=None, related_name="courier", on_delete=models.CASCADE)
    income = models.IntegerField()
    date = models.DateField()
