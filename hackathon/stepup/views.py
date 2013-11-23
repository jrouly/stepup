# Create your views here.

from django.shortcuts import render_to_response

# other view functions

# webpage-generating view functions
def index(request):

    return render_to_response('index.html', {

    },
    )

def opportunity(request):

    return render_to_response('opportunity.html', {

    },
    )

def person(request):
    return render_to_response('person.html', {

    },
    )

def organization(request):
    return render_to_response('organization.html', {

    },
    )
