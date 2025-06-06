from django import forms

from events.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=[
            "username",
            "password",
            "role",
            "first_name",
            "last_name",
            "email",
        ]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']