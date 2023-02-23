from django.core.exceptions import ValidationError
from django import forms
from .models import Publisher

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)

    search_in = forms.ChoiceField(required=False,choices=(("title", "Title"), ("contributor", "Contributor")))

# A form to input a new record into the Publishers table
class PublisherForm(forms.ModelForm):
    class Meta:
        """
        Pulls the fields from the Publisher table
        """
        model=Publisher
        fields = "__all__"
