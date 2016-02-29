'''
Created on Feb 27, 2016

@author: Pao
'''

from django import forms
from ballot.candidate_contants import PRESIDENT_CANDIDATES
from ballot.candidate_contants import VP_CANDIDATES
from ballot.candidate_contants import SENATE_CANDIDATES_1
from ballot.candidate_contants import SENATE_CANDIDATES_2

class VoteForm(forms.Form):
    president = forms.ChoiceField(choices=PRESIDENT_CANDIDATES, 
                                  required=True, 
                                  widget=forms.RadioSelect(attrs={'class' : 'pres-choices'}))
    
    vice_president = forms.ChoiceField(choices=VP_CANDIDATES, 
                                       required=True, 
                                       widget=forms.RadioSelect(attrs={'class' : 'vp-choices'}))
    
    senators_1 = forms.ChoiceField(choices=SENATE_CANDIDATES_1,
                                 required=True, 
                                 widget=forms.CheckboxSelectMultiple(attrs={'class' : 'senate-choices-1'}))
    
    senators_2 = forms.ChoiceField(choices=SENATE_CANDIDATES_2,
                             required=True, 
                             widget=forms.CheckboxSelectMultiple(attrs={'class' : 'senate-choices-2'}))
#     
    