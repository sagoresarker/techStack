from django.db import models


class TechStack(models.Model):
    url = models.URLField(unique=False)
    tech_info = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
