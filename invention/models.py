from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Invention(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = models.CharField(max_length=100)
    featured_video = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    inventor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("invention-detail", kwargs={"pk": self.pk})
