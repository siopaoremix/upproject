'''
Created on Feb 27, 2016

@author: Pao
'''

from django import forms

from ballot.candidate_contants import PRESIDENT_CANDIDATES
from ballot.candidate_contants import SENATE_CANDIDATES
from ballot.candidate_contants import VP_CANDIDATES
from ballot.candidate_contants import PARTY_LIST

class VoteForm(forms.Form):
    president = forms.ChoiceField(choices=PRESIDENT_CANDIDATES, 
                                  widget=forms.RadioSelect(attrs={'class' : 'pres-choices'}))
    
    vice_president = forms.ChoiceField(choices=VP_CANDIDATES, 
                                       widget=forms.RadioSelect(attrs={'class' : 'vp-choices'}))
   
    senators   = forms.ChoiceField(choices=SENATE_CANDIDATES,
                                   widget=forms.CheckboxSelectMultiple(attrs={'class' : 'senate-choices'}))
    
    party_list = forms.ChoiceField(choices=PARTY_LIST, 
                                       widget=forms.RadioSelect(attrs={'class' : 'party-choices'}))
       
    def clean(self):
        president_choice = self.cleaned_data.get('president')
        vp_choice = self.cleaned_data.get('vice_president')
        senators_choice = self.cleaned_data.get('senators')
        party_list_choice = self.cleaned_data.get('party_list')
 