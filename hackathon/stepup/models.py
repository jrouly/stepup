from django.db import models

# Create your models here.

class User(models.Model):
    """Default fields
    """

    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 50)
    # location =    
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        abstract = True

class Tag(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.name
class Opportunity(User):

class Person(User):

class Organization(User):
