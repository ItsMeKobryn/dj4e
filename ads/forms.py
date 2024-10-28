from django import forms
from ads.models import Ad

# Create the form class.
class CreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text', 'price', 'tags']  # Remove 'picture'

    # No need for picture validation or saving logic since the field is removed

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
