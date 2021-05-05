from django.db import models
from authentication.models import *
from SubscribersInventory.models import *

# Create your models here.

class AccountFile(models.Model):
    client_code      = models.ForeignKey(ClientCode, on_delete=models.CASCADE)
    client_full_name = models.ForeignKey(VOIPInformation, on_delete=models.CASCADE)
    file_name        = models.CharField(max_length=500, null=True, blank=True)
    url              = models.URLField(null=True, blank=True)
    file_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file_name

