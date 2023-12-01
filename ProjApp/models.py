# Create your models here.
from django.db import models
from autoslug import AutoSlugField

from ProjAppAuth.models import User

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class SourceCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Source(models.Model):
    LANGUAGE_CHOICES = (
        ('tamil', 'Tamil'),
        ('english', 'English'),
    )

    LEVEL = [("Basic", "Basic"), ("Intermediate", "Intermediate"), ("Advanced",
                                                                    "Advanced"), ("Project Based", "Project Based"), ("Topic Based", "Topic Based")]

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    telegram_name = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    category = models.ForeignKey(SourceCategory, on_delete=models.CASCADE)
    level = models.CharField(choices=LEVEL, max_length=100)
    channel_name = models.CharField(max_length=255)
    link = models.URLField()
    total_hits = models.PositiveIntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    ratings = models.PositiveIntegerField(default=0)
    total_ratings = models.PositiveIntegerField(default=0)
    total_rating_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.channel_name
