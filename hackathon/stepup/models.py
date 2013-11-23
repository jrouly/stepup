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

    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})
     
class Opportunity(User):

    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})

class Person(User):

    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})

class Organization(User):

    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})
