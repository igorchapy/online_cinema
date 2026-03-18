# src/commands/send_activation_emails.py
from app.services.email import send_activation_email
from app.models import ActivationToken

def run():
    tokens = ActivationToken.get_expired_tokens()
    for token in tokens:
        send_activation_email(token.user, token.token)
