from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    url_name = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.url_name:
            return reverse(self.url_name)
        return '#'

    def clean(self):
        if self.parent == self:
            raise ValidationError("Элемент не может быть родителем самого себя.")