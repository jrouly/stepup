# Create your views here.

from stepup.models import *
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# other view functions

#login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
	    return render_to_response('index.html', {

        },
        )
        else:
            # Return an 'invalid login' error message.
            return render_to_response('login.html', {
        },
        )
    else:
        return render_to_response('login.html', {
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

    return render_to_response('index.html', {

    },
    )
@login_required
def opportunity(request, slug):

    return render_to_response('opportunity.html', {
        # 'name' : 
    },
    )
@login_required
def person(request, slug):
    return render_to_response('person.html', {
    
    },
    )
@login_required
def organization(request, slug):
    return render_to_response('organization.html', {
    # put the variables you need here
    },
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
