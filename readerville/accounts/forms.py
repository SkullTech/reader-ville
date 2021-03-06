from django import forms
from django.urls import reverse
from .models import UserProfile
from libraries.models import Genre
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=50)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'loginForm'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('auth_login')

        self.helper.add_input(Submit('submit', 'Login'))


class ProfileForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), required=True,
                                            queryset=Genre.objects.all())

    class Meta:
        model = UserProfile
        exclude = ['user', 'bio']