from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_review_email(name: str, email: str, review: str):
    context = {
        'name': name,
        'email': email,
        'review': review
    }

    email_subject = "Thank you for your review"
    email_body = render_to_string('email_message.txt', context)

    email_message = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )

    return email_message.send(fail_silently=False)
