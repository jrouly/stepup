from django.contrib import admin
from stepup.models import Tag, Person, Organization, Opportunity

class OrgInlinePerson(admin.StackedInline):
    model = Organization.people.through
    extra = 1

class PersonInlineOrg(admin.StackedInline):
    model = Person.organizations.through
    extra = 1

class PersonInlineTag(admin.StackedInline):
    model = Tag.people.through
    extra = 1

class OpportunityInlineTag(admin.StackedInline):
    model = Tag.opportunities.through
    extra=1

class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'description']})
    ]
    list_display = ('name', 'description')

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'first_name', 'last_name', 'description']}),
        ("Location information", {'fields': ['city', 'state', 'country']})
    ]
    inlines = [PersonInlineOrg, PersonInlineTag]
    list_display = ('name', 'description')

class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,		{'fields': ['name', 'description']}),
	("Location information", {'fields': ['city', 'state', 'country']})
    ]
    inlines = [OrgInlinePerson]
    list_display = ('name', 'description')

class OpportunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'description']}),
        ("Location information", {'fields': ['city', 'state', 'country']})
    ]
    inlines = [OpportunityInlineTag]
    list_display = ('name', 'description')
    list_filter = ('name', 'tags', 'date_created')


admin.site.register(Tag, TagAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
