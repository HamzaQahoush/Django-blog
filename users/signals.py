from django.db.models.signals import post_save

from django.contrib.auth.models import User  # sender
from django.dispatch import receiver  # receiver
from .models import Profile


@receiver(post_save, sender=User, )
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
"""
when a user saved send a signal , this signal will received , receiver is the create profile function , 
and that function takes all the argument , create instance from user into profile model
"""


@receiver(post_save, sender=User, )
def save_profile(sender, instance, **kwargs):
    print(instance,'---instance')
    instance.profile.save()

"""
then we need to import these signals in app.py 
in ready function
"""