from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms


class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        label="Email", max_length=254, required=True,
        widget=forms.EmailInput(attrs={'class': 'input100'})
    )
    username = forms.CharField(required=False)  # Make username field optional

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()  # Hide the username field
        self.fields['password'].widget.attrs.update({'class': 'input100'})

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            try:
                user = User.objects.get(email__iexact=email)
                if user.check_password(self.cleaned_data['password']):
                    self.user_cache = authenticate(self.request, username=user.username, password=password)
            except ObjectDoesNotExist:
                self.user_cache = None

            if self.user_cache is None:
                raise self.get_invalid_login_error()

        return self.cleaned_data