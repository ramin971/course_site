from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    def __str__(self):
        return '{},({})'.format(self.name,self.address)

class Meetup(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='image')
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name='meetups')
    def __str__(self):
        return self.title
