from django.db import models

class user(models.Model):
    name = models.CharField ()
    id = models.AutoField(primary_key=True)
