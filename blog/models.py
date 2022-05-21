from django.conf import settings
from django.db import models
from django.utils import timezone


from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


User = get_user_model()

class Capital(models.Model):
    country = models.CharField('country', max_length=150)
    capital_city = models.CharField('capital', max_length=150)
    capital_population = models.IntegerField('population')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.capital_city