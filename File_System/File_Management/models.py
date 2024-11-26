from django.db import models

# Create your models here.
class Doccument(models.Model):
    title = models.CharField(max_length=100,default="")
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title