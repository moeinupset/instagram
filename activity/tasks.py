from time import sleep

from celery.task import task
from django.contrib.auth import get_user_model

User = get_user_model()


@task(name="Send Verification Code")
def send_verification_code(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExists:
        return None

    return user.username


@task(name="Send Verificaton Email")
def send_verification_email(email):
    sleep(10)
    print("email :", email)