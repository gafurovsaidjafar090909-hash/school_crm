from django import forms

from accounts.models import User

from .models import Parent


class ParentAdminForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = Parent
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "phone",
            "address",
        ]

    def save(self, commit=True):

        parent = super().save(commit=False)

        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        user = User.objects.create_user(
            username=username,
            password=password,
            role="parent",
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
        )

        parent.user = user

        if commit:
            parent.save()

        return parent