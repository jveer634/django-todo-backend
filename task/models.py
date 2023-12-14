from django.db import models

# Create your models here.
STATUS_CHOICES = [("TODO", "TODO"), ("IN PROGRESS", "IN PROGRESS"), ("DONE", "DONE")]


class Task(models.Model):

    title=models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    status= models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0], max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ["-created"]
        

    def __str__(self):
        return self.title

