from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib import auth

admin.autodiscover()

urlpatterns = patterns('stepup.views',
    # Examples:
    # url(r'^$', 'volunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #auth
    url(r'^login/', 'login_request', name = 'login'),
    url(r'^logout/', 'logout_page'),

    url(r'^admin/', include(admin.site.urls)),

    # homepage
    #url(r'^$', 'index', name = 'homepage'),

	# about
    url(r'^about$', 'about', name = 'view_about'),
    
    # person
    url(r'^person/(?P<slug>[^\.]+)', 'person', name = 'view_person'),

    # opportunity
    url(r'^opportunity/(?P<slug>[^\.]+)', 'opportunity', name = 'view_opportunity'),

    # organization
    url(r'^organization/(?P<slug>[^\.]+)', 'organization', name = 'view_organization'),

)
