from django import forms

class Rateing(forms.Form):
    rating = forms.FloatField(min_value=0, max_value=5, label='Please rate the course (0 to 10)')
