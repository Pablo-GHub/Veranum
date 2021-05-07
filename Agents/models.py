from django.db import models

# Create your models here.
class Agent(models.Model):

    class meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'Agents/images')

    def __str__(self):
        return self.name