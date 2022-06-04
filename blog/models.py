from django.db import models
from django.utils import timezone  # import timezone
from django.contrib.auth.models import User  # import user


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

    def __str__(self):
        return self.title
