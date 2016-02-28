from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ballot.forms import VoteForm

# Create your views here.

@login_required(login_url='/login/')
def hello(request):
    form = VoteForm()
    return render(request, 'hello.html', {'vote_form' : form})
