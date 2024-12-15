from django.contrib.auth.models import AbstractUser
from django.db import models


class Newspaper(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    publishers = models.ManyToManyField("Redactor", related_name="publishers")

    class Meta:
        ordering = ["published_date"]

    def __str__(self):
        return f"{self.title} ({self.published_date})"


class Topic(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"