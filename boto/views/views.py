'''
Created on Feb 21, 2016

@author: Pao
'''

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from boto.forms import LoginForm


def error(request):
    return render(request, 'error.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect('/vote')
#             if user.has_perms('ballot.can_view_vote_page'):
#                 return HttpResponseRedirect('/vote')
#             elif user.has_perms('dashboard.can_view_admin_page'):
#                 return HttpResponseRedirect('/admin')
#             else :
#                 pass
    return render(request, 'login.html', {'login_form': form })

@permission_required('dashboard.can_view_admin_page', login_url="/error/")
@login_required(login_url='/login/')
def admin_view(request):
    return HttpResponse('Admin')
