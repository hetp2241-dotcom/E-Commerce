from django.db import models

class PageView(models.Model):
    page = models.CharField(max_length=255)
    user_session = models.CharField(max_length=100, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page} - {self.viewed_at}"
