'''
Created on Feb 27, 2016

@author: Pao
'''

from django import forms
from ballot.candidate_contants import PRESIDENT_CANDIDATES
from ballot.candidate_contants import VP_CANDIDATES
from ballot.candidate_contants import SENATE_CANDIDATES

class VoteForm(forms.Form):
    president = forms.ChoiceField(choices=PRESIDENT_CANDIDATES, 
                                  required=True, 
                                  widget=forms.RadioSelect(attrs={'class' : 'pres-choices'}), 
                                  label='President')
    
    vice_president = forms.ChoiceField(choices=VP_CANDIDATES, 
                                       required=True, 
                                       widget=forms.RadioSelect(attrs={'class' : 'vp-choices'}), 
                                       label='Vice President')
    
    senators = forms.ChoiceField(choices=SENATE_CANDIDATES,
                                 required=True, 
                                 widget=forms.CheckboxSelectMultiple(attrs={'class' : 'senate-choices'}), 
                                 label='Senators')
#     
    