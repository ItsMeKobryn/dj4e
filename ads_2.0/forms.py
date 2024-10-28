from django import forms
from ads.models import Ad

# Create the form class.
class CreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text', 'price', 'tags']  # Remove 'picture' since it's no longer needed

    # The clean method and picture handling are no longer required since there is no image upload

    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()  # Save many-to-many relationships (like tags)
        return instance

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
