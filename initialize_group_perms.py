'''
Created on Feb 26, 2016

@author: Pao
'''

import django
django.setup()

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


def initialize_group_perms():
    admin_content_type = ContentType.objects.get(app_label='dashboard', model='results')
    student_content_type = ContentType.objects.get(app_label='ballot', model='vote')
    admin_perm = Permission(codename='can_view_admin_page',
                            name='Can view admin page',
                            content_type=admin_content_type)
    student_perm = Permission(codename='can_view_vote_page',
                              name='Can view vote page',
                              content_type=student_content_type)
    
    admin_perm = Permission.objects.filter(codename='can_view_admin_page')[0]
    student_perm = Permission.objects.filter(codename='can_view_vote_page')[0]
    
    admin_groups = Group.objects.filter(name='Admin')[0]
    student_groups = Group.objects.filter(name='Student')[0]
    
    admin_groups.permissions.add(admin_perm)
    student_groups.permissions.add(student_perm)
    
    u1 = User.objects.filter(username='user1')[0]
    u1.groups.add(admin_groups)
    
    print('end')

if __name__ == '__main__':
    initialize_group_perms()