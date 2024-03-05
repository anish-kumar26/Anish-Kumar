# techiehub/urls.py

from django.urls import path
from .views import login, home, CGIS_buisness, service, contact, about, loader, seller, cart, buy, iphone, service,signup, homework, hd_buyer, forgot_password,feedback_list, uniform_cleanliness, register, project_subbmision, student_marks, guest, layout, otp_verification, restart_signup, otp_password, The_enchanted_equinox, The_enchanted_equinox_quiz, The_Starlight_Symphony, The_Starlight_Symphony_quiz, payment, payment1, no_guest, sample3000, first_view, second_view, buisness, home_buy, home_and_buisness, generate_image, ai_chat, carpenter, buyer
from django.conf.urls.static import static
from django.urls import path
from .views import GmailView



urlpatterns = [
    path('first/', first_view, name='first_view'),
    path('seller/', seller, name='seller'),
    path('CGIS_buisness/', CGIS_buisness, name='CGIS_buisness'),
    path('buyer/', buyer, name='buyer'),
    path('hd_buyer/', hd_buyer, name='hd_buyer'),
    path('carpenter/', carpenter, name='carpenter'),
    path('ai_chat/', ai_chat, name='ai_chat'),
    path('generate_image/', generate_image, name='generate_image'),
    path('home_and_buisness/', home_and_buisness, name='home_and_buisness'),
    path('home_buy/', home_buy, name='home_buy'),
    path('buisness/', buisness, name='buisness'),
    path('second_view/', second_view, name='second_view'),
    path('The_enchanted_equinox/', The_enchanted_equinox, name='The_enchanted_equinox'),
    path('sample3000/', sample3000, name='sample3000'),
    path('payment/', payment, name='payment'),
    path('no_guest/', no_guest, name='no_guest'),
    path('payment1/', payment1, name='payment1'),
    path('The_Starlight_Symphony_quiz/', The_Starlight_Symphony_quiz, name='The_Starlight_Symphony_quiz'),
    path('The_Starlight_Symphony/', The_Starlight_Symphony, name='The_Starlight_Symphony'),
    path('The_enchanted_equinox_quiz/', The_enchanted_equinox_quiz, name='The_enchanted_equinox_quiz'),
    path('otp_password/', otp_password, name='otp_password'),
    path('restart_signup/', restart_signup, name='restart_signup'),
    path('feedback/', feedback_list, name='feedback_list'),
    path('otp_verification/', otp_verification, name='otp_verification'),
    path('layout/', layout, name='layout'),
    path('guest/', guest, name='guest'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('student_marks/', student_marks, name='student_marks'),
    path('project_subbmision/', project_subbmision, name='project_subbmision'),
    path('register/', register, name='register'),
    path('uniform_cleanliness/', uniform_cleanliness, name='uniform_cleanliness'),
    path('signup/', signup, name='signup'),
    path('homework/', homework, name='homework'),
    path('', login, name='login'),
    path('home/', home, name='home'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('loader/', about, name='loader'),
    path('', home, name='home'),
    path('gmail/', GmailView.as_view(), name='gmail'),
    path('cart/', cart, name='cart'),
    path('buy/<int:product_id>/', buy, name='buy'),
    path('iphone/', iphone, name='iphone'),
    path('service/', service, name='service'),
    path('loader/', loader, name='loader'),    
]


