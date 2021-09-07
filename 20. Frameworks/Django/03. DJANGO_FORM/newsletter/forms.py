from django import forms


class MailForm(forms.Form):
    # widget, attrs 옵션은 HTML을 만들기 위해 존재함!
    name = forms.CharField(max_length=10, min_length=2, required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(label='메일내용', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': '입력!'
    }))
    check = forms.BooleanField(required=False)