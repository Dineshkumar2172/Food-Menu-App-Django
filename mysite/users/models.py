from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # one to one relationship between user mode and profile model
    # each user will have one profile and each profile belongs to single user
    # defining 1-1 relationship between profile and user
    # also configuring to delete profile whenever a user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        # returning username from user model mapped earlier
        # we can access all the fields from user mode inside here since we are inheriting it here
        return self.user.username
