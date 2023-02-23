from django.core.exceptions import ValidationError
from django import forms
from .models import Publisher, Review

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)

    search_in = forms.ChoiceField(required=False,choices=(("title", "Title"), ("contributor", "Contributor")))

# A form to input a new record into the Publishers table
class PublisherForm(forms.ModelForm):
    class Meta:
        """
        Pulls the fields from the Publisher model
        """
        model = Publisher
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        """
        Pulls the fields from the Review model
        """
        model = Review
        exclude = ["date_edited", "book"]

    rating = forms.IntegerField(min_value=0, max_value=5)