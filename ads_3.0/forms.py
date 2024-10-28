from django import forms
from ads.models import Ad

# Create the form class.
class CreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text', 'price']  # Removed 'picture'

    # No need to validate or process any file, since picture field is removed
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
