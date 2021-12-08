from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

class Reservations(models.Model):
    title = models.CharField(max_length=200, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    number_of_quests = models.IntegerField
    Date = models.DateField(auto_now_add=False)
    Time = models.TimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
