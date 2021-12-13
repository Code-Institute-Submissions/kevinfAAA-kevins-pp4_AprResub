from django.db import models
from django.contrib.auth.models import User



STATUS = ((0, "Draft"), (1, "Published"))

class Reservations(models.Model):
    title = models.CharField(max_length=200, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", default=1)
    number_of_guests = models.IntegerField(default=1)
    date = models.DateField()
    time = models.TimeField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
