from django.db import models

# Create your models here.
class Candidate(models.Model):
    pass

class Vote(models.Model):
    class Meta:
        permissions = (('can_view_vote' , 'Can view vote page'),)

class HasVote(models.Model):
    pass