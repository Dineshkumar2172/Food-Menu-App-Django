from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("myapp:home")

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=2000)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default='https://theme-assets.getbento.com/sensei/193414f.sensei/assets/images/catering-item-placeholder-704x520.png')
