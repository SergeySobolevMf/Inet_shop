from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=20, default='--пусто--')
    slug = models.SlugField(unique=True, default='slug')
    description = models.TextField()

    def __str__(self):
        return self.title


class Mobile(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=20)
    description  = models.TextField()
    price = models.IntegerField()
    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mobiles'
    )
    group = models.ForeignKey( 
        Group, 
        on_delete=models.PROTECT, 
        blank=True, 
        null=True, 
        related_name='mobiles' 

    ) 

    class Meta:
        ordering = ['name']


