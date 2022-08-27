from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings


def send_email_verification(request, user):
    # send Verification
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    mail_subject = " Please Activate your Account"
    message = render_to_string("account/account_verification_email.html", {
        "user": user,
        "domain": current_site,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user),

    })

    to_email = user.email
    send_email = EmailMessage(mail_subject, message, from_email, to=[to_email])

    send_email.send()


def send_password_reset_verification(request, user):
    current_site = get_current_site(request)
    email_subject = "Create a new  Password"
    message = render_to_string("account/reset_password_email.html", {
        "user": user,
        "domain": current_site,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user)
    })

    email_to = user.email
    send_email = EmailMessage(
        email_subject, message, to=[email_to])
    send_email.send()
