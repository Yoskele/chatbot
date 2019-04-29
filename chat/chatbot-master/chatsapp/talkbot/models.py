from django.db import migrations, models
from django.contrib.auth.models import User


# Create your models here.
class ChattRoom(models.Model):
    message = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.message
