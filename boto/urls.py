from django.conf.urls import patterns, include, url
from django.contrib import admin as superadmin

from ballot.views import vote
from boto.views.views import login_view as login
from boto.views.views import admin_view as admin
from boto.views.views import error

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^super-admin/', include(superadmin.site.urls)),
    url(r'^admin/', admin),
    url(r'^hello/', vote),
    url(r'^login/', login),
    url(r'^error/', error),
)
