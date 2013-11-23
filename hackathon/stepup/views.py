# Create your views here.

from stepup.models import *
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

# other view functions

# webpage-generating view functions
def index(request):

    # opportunities filtered by user's tags, and in reverse chronological order

    opportunities = Opportunity.objects.filter(tags__).order_by("-posted")
    paginator = Paginator(opportunities, 12)

    try:
         page = int(request.GET.get("page", '1'))
    except ValueError:
         page = 1

    try: 
        opportunities = paginator.page(page)
    except (InvalidPage, EmptyPage):
        opportunities = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {

    },
    )

def opportunity(request, slug):

    return render_to_response('opportunity.html', {
        # 'name' : 
    },
    )

def person(request, slug):
    return render_to_response('person.html', {
    
    },
    )

def organization(request, slug):
    return render_to_response('organization.html', {
    # put the variables you need here
    },
    )
