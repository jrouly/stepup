from django.contrib import admin
from stepup.models import Tag, Person, Organization, Opportunity

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Tag, TagAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Organization, OrganizationAdmin)
