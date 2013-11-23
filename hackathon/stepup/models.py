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

<<<<<<< HEAD
    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})
     
=======
    def __unicode__(self):
        return '%s' % self.name
>>>>>>> 8d2caacf150bd42121359d75f0df410a745c5b90
class Opportunity(User):

    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})

class Person(User):

<<<<<<< .merge_file_ZutE4E
    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})
=======
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
>>>>>>> .merge_file_7TotPB

class Organization(User):

    @permalink
    def get_absolute_url(self):
        return ('name_of_the_view;, None, {'slug':self.slug})
