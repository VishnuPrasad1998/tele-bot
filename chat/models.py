from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Buttonhits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    fat_hits = models.IntegerField(default=0)
    dumb_hits = models.IntegerField(default=0)
    stupid_hits = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username