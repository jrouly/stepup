from django.db import models

# Create your models here.


class User(models.Model):
    """Default fields
    """

    name = models.CharField("Username", max_length=200)
    slug = models.SlugField(max_length=50)
    # location =
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        abstract = True


class Opportunity(models.Model):
    name = models.CharField("Name", max_length=200)
    slug = models.SlugField(max_length=50)
    description = models.TextField()

    tags = models.ManyToManyField('Tag')
    organizations = models.ManyToManyField('Organization')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    schedule = models.DateField()
    date_created = models.DateTimeField()
    date_created.auto_now_add = True
    @models.permalink
    def get_absolute_url(self):
        return ('name_of_the_view', None, {'slug': self.slug})

    def __unicode__(self):
            return '%s' % self.name

    class Meta:
        verbose_name_plural = "Opportunities"


class Person(User):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    schedule = models.DateField()
    tags = models.ManyToManyField('Tag')
    organizations = models.ManyToManyField('Organization')

    @models.permalink
    def get_absolute_url(self):
        return ('name_of_the_view', None, {'slug': self.slug})

    class Meta:
        verbose_name_plural = "People"


class Organization(User):
    people = models.ManyToManyField(Person, Person.organizations.through,
                                    blank=True)
    opportunities = models.ManyToManyField(Opportunity,
                                           Opportunity.organizations.through,
                                           blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    @models.permalink
    def get_absolute_url(self):
        return ('name_of_the_view', None, {'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    people = models.ManyToManyField(Person, through=Person.tags.through,
                                    blank=True)
    opportunities = models.ManyToManyField(Opportunity,
                                           through=Opportunity.tags.through,
                                           blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('name_of_the_view', None, {'slug': self.slug})

    def __unicode__(self):
        return '%s' % self.name
