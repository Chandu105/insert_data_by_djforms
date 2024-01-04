from django import forms

class SchoolForm(forms.Form):
    Sname=forms.CharField()
    Slocation=forms.CharField()
    Sprincipal=forms.CharField()