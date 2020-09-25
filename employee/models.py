from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from business.models import Business


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bussiness = models.ForeignKey(Business,on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=20, null=True, blank=True)
    employee_name = models.CharField(max_length=100)
    employee_sal = models.PositiveIntegerField(null=True, blank=True)
    pruduct_details = models.CharField(max_length=200, null=True, blank=True)
    user_image = models.ImageField(upload_to='employees/')

    def __str__(self):
        return self.user.username


@receiver(post_delete, sender=Employee)
def submission_delete(sender, instance, **kwargs):
	instance.user_image.delete(False)

class ProfitModel(models.Model):
    user = models.OneToOneField(Employee,on_delete=models.CASCADE)
    income = models.IntegerField(blank=True, null=True)
    expense = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)