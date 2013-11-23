# Create your views here.

from stepup.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# other view functions

#login

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
	    return render_to_response('/', {

        },
        )
        else:
            # Return an 'invalid login' error message.
            return render_to_response('/login', {
        },
        )
    else:
        return render_to_response('/login', {
        },
        )

# webpage-generating view functions
@login_required
def index(request):

    # opportunities filtered by user's tags, and in reverse chronological order

#    opportunities = Opportunity.objects.all().order_by("-posted")
#    paginator = Paginator(opportunities, 12)

#    try:
#         page = int(request.GET.get("page", '1'))
#    except ValueError:
#         page = 1

#    try: 
#        opportunities = paginator.page(page)
#    except (InvalidPage, EmptyPage):
#        opportunities = paginator.page(paginator.num_pages)

    current_user = Person.objects.get(user__username=request.user.username)

    tag_opportunities = []
    current_tags = current_user.tags.all()
    for tag in current_tags:
        opportunity = Opportunity.objects.filter(tags=tag).all()
        tag_opportunities.append( opportunity )

    org_opportunities = []
    current_orgs = current_user.organizations.all()
    for org in current_orgs:
        opportunity = Opportunity.objects.filter(organizations=org).all()
        org_opportunities.append( opportunity )

    tags_and_orgs = []
    global_tags = Tag.objects.all()
    for tag in global_tags:
        tags_and_orgs.append( tag )
    global_orgs = Organization.objects.all()
    for org in global_orgs:
        tags_and_orgs.append( org )

    global_opps = Opportunity.objects.all()

    return render_to_response('index.html', {
        "current_user" : current_user,
        "tag_feed" : tag_opportunities,
        "org_feed" : org_opportunities,
        "tags_and_orgs_feed" : tags_and_orgs,
        "combined_feed" : global_opps,
    },
    context_instance = RequestContext(request),
    )

@login_required
def opportunity(request, slug):
    return render_to_response('opportunity.html', {
        # 'name' : 
    },
    context_instance = RequestContext(request),
    )

@login_required
def person(request, slug):
    return render_to_response('person.html', {
        "current_user" : request.user,
        "requested_user" : Person.objects.get(user__username=slug),
        "requested_tags" : Person.objects.get(user__username=slug).tags.all(),
        #"global_tags" : Tag.objects.all(),
        "global_events" : Opportunity.objects.all(),
        "sunday" : len(Person.objects.get(user__username=slug).sunday),
        "monday" : len(Person.objects.get(user__username=slug).monday),
        "tuesday" : len(Person.objects.get(user__username=slug).tuesday),
        "wednesday" : len(Person.objects.get(user__username=slug).wednesday),
        "thursday" : len(Person.objects.get(user__username=slug).thursday),
        "friday" : len(Person.objects.get(user__username=slug).friday),
        "saturday" : len(Person.objects.get(user__username=slug).saturday),
    },
    context_instance = RequestContext(request),
    )

@login_required
def organization(request, slug):
    return render_to_response('organization.html', {
    # put the variables you need here
    },
    context_instance = RequestContext(request),
    )

@login_required
def search(request):
    return render_to_response('search.html', {
    },
    context_instance = RequestContext(request),
    )

def about(request):
    return render_to_response('about.html', {
    # put the variables you need here
    },
    )

def logout_page(request, slug):
    logout(request)
    return render_to_response('login.html', {
    # put the variables you need here
    },
    )
