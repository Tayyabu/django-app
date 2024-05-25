from django.core.mail import send_mail
from blog.settings import EMAIL_HOST_USER

def send_email_to_client():
    send_mail(subject="hey",message="I am Django",from_email=EMAIL_HOST_USER,recipient_list=["tb3286427@gmail.com"])


