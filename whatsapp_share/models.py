"""
"""
from django.db import models
from django.contrib.auth.models import User
from settings import MEDIA_URL

class Item(models.Model):
    """
    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='items')
    inventory = models.PositiveIntegerField(default=0)
    creation_dt = models.DateTimeField(auto_now_add=True)
    modification_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'items'

    def __str__(self):
        return "%d - %s" % (self.id, self.name)

    @property
    def get_absolute_image_url(self):
        try:
            return "{0}{1}".format(MEDIA_URL, self.image.url.replace('/media/', ''))
        except:
            return "{0}{1}".format(MEDIA_URL, 'items/default.jpg')


class Purchase(models.Model):
    """
    """
    item = models.ForeignKey(Item, blank=True, related_name='item')
    buyer = models.ForeignKey(User, related_name='buyer')
    purchased_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return "%d - %s" % (self.id, self.item.name)
