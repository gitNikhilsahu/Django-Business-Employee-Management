from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_id = models.CharField(max_length=20)
    business_name = models.CharField(max_length=100)
    business_image = models.ImageField(upload_to='bussiness/')
    
    def __str__(self):
        return self.business_name

@receiver(post_delete, sender=Business)
def submission_delete(sender, instance, **kwargs):
	instance.business_image.delete(False)
