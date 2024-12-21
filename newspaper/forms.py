from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator, MaxValueValidator

from newspaper.models import Redactor, Newspaper


class RedactorCreationForm(UserCreationForm):
    years_of_experience =forms.IntegerField(
        label='Years of experience',
        required=True,
        validators=[MinValueValidator(0), MaxValueValidator(30)]
    )

    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class RedactorExperienceForm(forms.ModelForm):
    years_of_experience =forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0), MaxValueValidator(30)]
    )

    class Meta:
        model = Redactor
        fields = ("years_of_experience",)


class NewspaperForm(forms.ModelForm):
    model = Newspaper
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Newspaper
        fields = "__all__"