from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.forms import SetPasswordForm


class UserProfileForm(forms.ModelForm):
    # Add fields for first_name and last_name
    first_name = forms.CharField(
        max_length=30, required=True, label="First Name")
    last_name = forms.CharField(
        max_length=30, required=True, label="Last Name")

    photo = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'clearablefileinput'}), label='Profile photo')

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profession',
                  'city', 'phone',  'photo']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Include first_name and last_name fields from the User model
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        # Save the first_name and last_name fields back to the User model
        self.instance.user.first_name = self.cleaned_data['first_name']
        self.instance.user.last_name = self.cleaned_data['last_name']

        # Save the UserProfile instance
        user_profile = super(UserProfileForm, self).save(commit=commit)

        if commit:
            # Save the User model
            self.instance.user.save()

        return user_profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Email address'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()

        # Create the user profile
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        # Update user profile attributes
        user_profile.first_name = user.first_name
        user_profile.last_name = user.last_name
        user_profile.save()

        return user


class UserPasswordChangeForm(SetPasswordForm):
    """
    For changing password
    """
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
    )

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.user
        if user.check_password(old_password):
            return old_password
        else:
            raise forms.ValidationError("The old password is incorrect.")

    def __init__(self, *args, **kwargs):
        """
        updating form
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
            
