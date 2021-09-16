from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """ slide code
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
    
    """
    class Meta(UserChangeForm.Meta):
        # username 은 변경 불가능하게!
        fields = ('first_name', 'last_name', 'email')




# class CustomUserChangeForm(forms.ModelForm):

#     class Meta(UserChangeForm.Meta):
#         model = get_user_model()
#         fields = ('first_name', 'last_name', 'email')