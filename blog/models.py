from django.db import models
from django.utils import timezone  # import timezone
from django.contrib.auth.models import User  # import user
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    # default : to allow to change  the date time.
    # auto_now=True=> update the time for everytime we change.
    # auto_now_add=True=> for the time we created . we cannot edit
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # on_delete=models.CASCADE => tell django to delete post if user deleted.
    class Meta:
        ordering = ['-data_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        redirect : for specific route.
        reverse : return the full url as string.
        find django url to find any post url
        :return: path for specific post
        """
        return reverse('post-detail', kwargs={'pk': self.pk})
