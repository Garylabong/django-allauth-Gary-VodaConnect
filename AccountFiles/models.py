from django.db import models
from authentication.models import *
from SubscribersInventory.models import *

# Create your models here.


class AccountFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    client_code = models.ForeignKey(ClientCode, on_delete=models.CASCADE)
    client_full_name = models.CharField(max_length=500, null=True, blank=True)
    file_name = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    file_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file_name
