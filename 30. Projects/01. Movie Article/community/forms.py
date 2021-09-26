from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    movie_title = forms.CharField(max_length = 100)
    title = forms.CharField(max_length = 100)

    class Meta:
        model = Review
        fields = '__all__'