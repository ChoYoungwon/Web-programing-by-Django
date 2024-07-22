from django.db import models

class bookmark(models.Model):
    title = models.CharField('Title', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.title
