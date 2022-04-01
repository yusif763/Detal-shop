from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,PasswordResetForm,\
SetPasswordForm
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from django.utils.safestring import mark_safe
from string import Template

User = get_user_model()


# from string import Template
# from django.utils.safestring import mark_safe
# from django.forms import ImageField

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'user-form-input',
                                          'placeholder': 'Password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'user-form-input',
                                          'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'phone',
            'is_market',
            'adress',
            'image',
            'password1',
            'password2',

        )
        choices = ['Satici',"Alici"]

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'First name'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'Phone'
            }),
            'is_marketd': forms.CheckboxInput(attrs={
                'class':'user-select-is-market',
                'sozunu':'marketsinqizmi'
            }),
            # 'is_market': forms.ChoiceField(),
            #  'is_market': forms.Select(attrs={
            #     'class': 'user-form-input',
            #     'placeholder': 'Satici ?'
            # }),
            'adress': forms.TextInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'Adress'
            }),
            # 'image':forms.FileField()
}           

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('password and confirm password is not same')
        return super().clean()



class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={
        'class': 'login-input',
        'placeholder': 'Email'
    }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': 'login-input',
        'placeholder': 'Password'
    }))
    
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 
        'autofocus': True,
        'class': 'user-form-input',
        'placeholder': 'Old Password',
        }),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
        'class': 'user-form-input',
        'placeholder': 'New Password',
            }),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
        'class': 'user-form-input',
        'placeholder': 'Confirm New Password',
        }),
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'user-form-input',
            'placeholder': _('Email'),
        })
    )


class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'user-form-input',
        'placeholder': 'New Password',}),
        strip=False,
        help_text=password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'user-form-input',
        'placeholder': 'New password confirmation',}),
    )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'phone','adress')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name',
            }),
            
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'Phone'
            }),
            'adress': forms.TextInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'Address'
            }),

        }