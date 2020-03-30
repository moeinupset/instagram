from time import sleep
from kavenegar import *
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


@task(name='Send Sms')
def send_sms_api_kavenegar():
    phone_number = list(User.objects.values_list('phone_number', flat=True))
    try:
        import json
    except ImportError:
         import simplejson as json
    try:
        api = KavenegarAPI('526D567247776C726F39476E6E4F474A2B2F733369346559626C66336754544964627331697A535A3774553D')
        print(api)
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': 'سلام خوبی ؟',
        }
        print(params)
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
