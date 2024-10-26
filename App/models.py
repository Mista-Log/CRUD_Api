from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    level= models.IntegerField()
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    