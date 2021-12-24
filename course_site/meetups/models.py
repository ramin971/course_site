from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    def __str__(self):
        return '{},({})'.format(self.name,self.address)

class Participant(models.Model):
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.email

class Meetup(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    date=models.DateField()
    organizer_email=models.EmailField()
    description=models.TextField()
    image=models.ImageField(upload_to='image')
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name='meetups')
    participant=models.ManyToManyField(Participant,blank=True,null=True,related_name='meetups')

    def get_participant(self):
        return ",\n".join([str(p) for p in self.participant.all()])

    def __str__(self):
        return self.title
