from django import forms
from django.contrib.auth import get_user_model

from .models import Teacher

User = get_user_model()


class TeacherAdminForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = Teacher
        fields = (
            "username",
            "password",
            "name",
            "surname",
            "phone",
            "subjects",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.user:
            self.fields["username"].initial = self.instance.user.username

    def save(self, commit=True):

        teacher = super().save(commit=False)

        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if teacher.user:
            user = teacher.user
            user.username = username

            if password:
                user.set_password(password)

            user.save()

        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )

            teacher.user = user

        if commit:
            teacher.save()
            self.save_m2m()

        return teacher