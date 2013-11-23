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

    
class Opportunity(User):

class Person(User):

	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	bio = models.TextField(max_length = 2048)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	country models.CharField(max_length = 50)
	schedule = models.DateField()
	tags = models.ForeignKey('Tag')

	def __unicode__(self):
		return '%s' % self.name

class Organization(User):
