from django.db import models

# Create your models here.
class Candidate(models.Model):
    pass

class Vote(models.Model):
    student_id = models.ForeignKey(Student)
    candidate_id = models.ForeignKey(Candidate)
    position = models.CharField()

    class Meta:
        permissions = (('can_view_vote' , 'Can view vote page'),)

class HasVote(models.Model):
    pass