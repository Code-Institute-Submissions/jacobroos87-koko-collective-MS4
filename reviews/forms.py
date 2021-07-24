from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """
    Form for user to add reviews
    """
    class Meta:
        model = Reviews
        exclude = (
            'user',
            'date_posted',
            'date_updated',
            'product',)

        fields = ['title', 'description', 'rating']

        labels = {
            'rating': 'Rating',
        }

    def __init__(self, *args, **kwargs):
        """
        Placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Description',
        }

        # Add placeholders and classes to input fields
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = (
                'mb-3 rounded-0')
