from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('stepup.views',
    # Examples:
    # url(r'^$', 'volunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #auth
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', 'logout_page'),

    url(r'^admin/', include(admin.site.urls)),

    # homepage
    url(r'^$', 'index', name = 'homepage'),

    # person
    url(r'^person/(?P<slug>[^\.]+)', 'person', name = 'view_person'),

    # opportunity
    url(r'^opportunity/(?P<slug>[^\.]+)', 'opportunity', name = 'view_opportunity'),

    # organization
    url(r'^organization/(?P<slug>[^\.]+)', 'organization', name = 'view_organization'),

    # about
    url(r'^about/(?P<slug>[^\.]+)', 'about', name = 'view_about'),

)
