from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib import auth

admin.autodiscover()

urlpatterns = patterns('stepup.views',
    # Examples:
    # url(r'^$', 'volunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #auth

    url(r'^admin/', include(admin.site.urls)),

    # homepage
    url(r'^$', 'index', name = 'homepage'),

    # about
    url(r'^about/$', 'about', name = 'view_about'),
    
    # person
    url(r'^person/(?P<slug>[^\.]+)', 'person', name = 'view_person'),

    # all persons
    url(r'^person/', 'all_person', name = 'view_all_person'),

    # opportunity
    url(r'^opportunity/(?P<slug>[^\.]+)', 'opportunity', name = 'view_opportunity'),

    # all opportunities
    url(r'^opportunity/', 'all_opportunity', name = 'view_all_opportunity'),

    # organization
    url(r'^organization/(?P<slug>[^\.]+)', 'organization', name = 'view_organization'),

    #url(r'^tag/(?P<slug>[^\.]+)', 'tag', name = 'view_tag'),
    
    # all organizations
    url(r'^organization/', 'all_organizations', name = 'view_all_organization'),

    # comments
    url(r'^comments/', include('django.contrib.comments.urls')),

    # search
    url(r'^search/', 'search', name = 'view_search'),

)
#urlpatterns += patterns('',
#    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login_request'}, name='user-login')
#)
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='mysite_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='mysite_logout'),
)
