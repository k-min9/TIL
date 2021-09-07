from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        # fieds / exclude 는 모델의 필드에만 적용됨.
        fields = '__all__'
        # fields = ('title', 'content', )