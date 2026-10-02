from django import forms
from django.contrib.auth import get_user_model

from .models import Student

User = get_user_model()


class StudentAdminForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = Student
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "date_of_birth",
            "phone",
            "address",
            "parent",
            "class_room",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.user:
            self.fields["username"].initial = self.instance.user.username

    def save(self, commit=True):

        student = super().save(commit=False)

        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if student.user:

            user = student.user
            user.username = username

            if password:
                user.set_password(password)

            user.save()

        else:

            user = User.objects.create_user(
                username=username,
                password=password
            )

            student.user = user

        if commit:
            student.save()
            self.save_m2m()

        return student