from django import forms

class UserForm(forms.Form):
    your_location = forms.CharField(label='Your Location', max_length = 100)
    your_search_radius = forms.IntegerField(label='Search Radius')
    your_star_standard = forms.DecimalField(label='Star Requirement', max_digits=2, decimal_places=1)
