from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ballot.forms import VoteForm

# Create your views here.

@login_required(login_url='/login/')
def vote(request):
    form = VoteForm()
    return render(request, 'ballot.html', {'vote_form' : form})
