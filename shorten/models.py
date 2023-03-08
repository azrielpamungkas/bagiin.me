
from django.db import models
from django.utils import timezone


# Create your models here.
class Shorten(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField()
    slug = models.SlugField(blank=True)
    password = models.CharField(max_length=100,null=True, blank=True)
    createdate = models.DateTimeField(default=timezone.now)


    def save(self, *args, **kwargs):
        self.title = self.id
        return super(Shorten,self).save(*args, **kwargs)
