from django.db import models
# Create your models here.
import random

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Paste(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default="text", max_length=100)
    new_paste = models.TextField(verbose_name="New Paste")
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'%s (%s)' % (self.title, self.language)
