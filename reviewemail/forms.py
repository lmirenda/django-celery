from django import forms
from django.core.exceptions import ValidationError

from reviewemail.models import ReviewDB
from reviewemail.tasks import send_review_email_task


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewDB
        fields = '__all__'

    name = forms.CharField(
        label="Firstname", min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-first-name'}
        )
    )
    email = forms.EmailField(
        label='Email', max_length=200, widget=forms.EmailInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email@email.com', 'id': 'form-email'}
        )
    )
    review = forms.CharField(
        label="Review", widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '5'}
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@lightit.io'):
            raise ValidationError("Email must end with @lightit.io")
        return email

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['review']
        )
