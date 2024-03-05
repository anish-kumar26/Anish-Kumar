from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.views import View
from .forms import FeedbackForm
from datetime import datetime
from .models import Student
from .forms import UserRegistrationForm
from .models import Feedback
from twilio.rest import Client
import random
from django.http import HttpResponse
from django.http import JsonResponse
from twilio.base.exceptions import TwilioRestException
from PIL import Image, ImageDraw
import time
import random
from django.http import HttpResponse
from io import BytesIO
from django.http import JsonResponse
import openai
from .models import Product
from decimal import Decimal

def seller(request):

    return render(request, 'seller.html')

def buyer(request):
    name = request.POST.get('name')
    dor = request.POST.get('dor')
    dob = request.POST.get('dob')
    old_address = request.POST.get('old_address')
    new_address = request.POST.get('new_address')
    number = request.POST.get('number')
    print(name)
    print(dor)
    print(dob)
    print(old_address)
    print(new_address)
    print(number)


    return render(request, 'buyer.html')

def sold_products(request):
    sold_products = Product.objects.all()
    return render(request, 'sold_products.html', {'sold_products': sold_products})


openai.api_key = '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'
def ai_chat(request):
    if request.method == 'POST':
        print("Conversation has started by User")
        user_input = request.POST.get('user_input')

        request_image = "image" in user_input.lower() or "picture" in user_input.lower()

        conversation_history = [
        {"role": "system", "content": "You are a helpful assistant created by Anish Kumar."},
        {"role": "system", "content": "You are created in chennai."},
        {"role": "system", "content": "Mainly you are not an product of openai your turbo made by Anish Kumar do not use an word of openai Do not say openai or chatgpt YOU ARE TURBO"},
        {"role": "system", "content": "You are named turbo."},
        {"role": "system", "content": "Anish kumar is an very good programer and an very good pianist and he programed you(turbo) and he programed the stylish heaven wensite and he is te ceo of stylish heaven and turbo and he is very populer in the place chennai and he is studying 5th and in casagrand international school"},
        {"role": "user", "content": "You are has to be helpful for the website named StyilishHeaven that is an interior designing website and StylishHeaven is created by the owner of the Turbo AI Anish kumar"},
        {"role": "user", "content": user_input}
        ]
        if request_image:
            print("Image requested by User")
            print("image requested:", user_input)
            image_response = openai.Image.create(
                prompt=user_input,
                n=1,
                size="256x256",
                
            )
            print("Image URL: " ,image_response)
            


            ai_reply = image_response["data"][0]["url"]
        else:

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
                max_tokens=1500
            )

            ai_reply = response['choices'][0]['message']['content']
            print("User input: ", user_input)
            print("AI's reply: ", ai_reply)

        return JsonResponse({'ai_response': ai_reply})

    elif request.method == 'GET':
        return render(request, 'ai_chat.html')




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        name_on_card = request.POST.get('name_on_card')
        ccv = request.POST.get('ccv')
        card_brand = request.POST.get('card_brand')
        coupon_code = request.POST.get('coupon_code')
        phone_number = request.POST.get('phone_number')
        print("Payment done for book")
        print("Card Number:", card_number)
        print("Phone Number:", phone_number)
        print("Name:", name_on_card)
        print("CCV:", ccv)
        print("Brand:", card_brand)
        print("Coupon:", coupon_code)

        return HttpResponseRedirect(reverse('The_enchanted_equinox'))

    return render(request, 'payment.html')

def payment1(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        name_on_card = request.POST.get('name_on_card')
        ccv = request.POST.get('ccv')
        card_brand = request.POST.get('card_brand')
        coupon_code = request.POST.get('coupon_code')

        
        print("Payment done for book")
        print("Card Number:", card_number)
        print("Name:", name_on_card)
        print("CCV:", ccv)
        print("Brand:", card_brand)
        print("Coupon:", coupon_code)


        return HttpResponseRedirect(reverse('The_Starlight_Symphony'))

    return render(request, 'payment1.html')
    

def uniform_reports(request):
    return render(request, 'uniform_reports.html')

def CGIS_buisness(request):
    return render(request, 'CGIS_buisness.html')


def no_guest(request):
    return render(request, 'no_guest.html')


def student_marks(request):
    return render(request, 'student_marks.html')


def homework(request):
    return render(request, 'homework.html')



def project_subbmision(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectName')
        print(project_name)
        return render(request, 'project_subbmision.html', {'projectName': project_name})
    else:
        return render(request, 'project_subbmision.html')





def cart(request):

    return render(request,'cart.html')

def buy(request):
     return render(request,'buy.html')

def iphone(request):
    return render(request, 'iphone.html')


class GmailView(View):
    template_name = 'gmail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        from_email = request.POST.get('from_email')
        to_email = request.POST.get('to_email')
        message = request.POST.get('message')
        print("Gmail Recived From", from_email)
        print("Gmail sent to", to_email)
        print("Gmail - ",message)
        success_message = "Email sent successfully!"

        return render(request, self.template_name, {'success_message': success_message})




def home(request):
    return render(request, 'Techiehub/home.html')

def layout(request):
    return render(request, 'Techiehub/layout.html')

def updates(request):
    return render(request, 'updates.html')






def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Logined As", username)
        print("Password is", password)
        
        if username == 'anishtechie20@gmail.com' and password == 'welcome0@123':
            my_variable = "Anish"

            
        elif username == 'sidharth@gmail.com' and password == 'sidharth@123':
            my_variable = "Sidharth"
        elif username == 'samueltennysonfranklin@gmail.com' and password == 'kakapee@123':
            my_variable = "Samuel"
        elif username == 'sourouw20@gmail.com' and password == 'sourouw123':
            my_variable = "Sourow"
        elif username == 'harshan12@gmail.com' and password == 'harshan@123':
            my_variable = "Harshan Loose"
        elif username == 'hajim@gmail.com' and password == 'haasimm121':
            my_variable = "Hasim"


        else:
            error_message = 'Enter the correct username and password.'
            return render(request, 'login.html', {'error_message': error_message})

        request.session['my_variable'] = my_variable

        return render(request, 'techiehub/home.html', {'my_variable': my_variable})

    return render(request, 'login.html')

def sample3000(request):
    my_url = request.session.get('my_url')
    print(my_url)
    return render(request, 'sample3000.html')

def first_view(request):
    my_url = "login"
    return render(request, 'my_template.html', {'my_url': my_url})

def second_view(request):
    old_url = request.GET.get('old_url', '/default/')

    return render(request, 'my_template.html', {'old_url': old_url})


def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback_app/feedback_list.html', {'feedbacks': feedbacks})




def generate_image(request):

    frames = []

    for _ in range(10): 
        image = Image.new('RGB', (300, 300), color='white')
        draw = ImageDraw.Draw(image)

      
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x0, x1 = sorted([random.randint(50, 250), random.randint(150, 300)])
        y0, y1 = sorted([random.randint(50, 250), random.randint(150, 300)])
        random_coordinates = [x0, y0, x1, y1]


        draw.ellipse(random_coordinates, fill=random_color)
        frames.append(image)

    gif_buffer = BytesIO()
    frames[0].save(gif_buffer, format='GIF', save_all=True, append_images=frames[1:], duration=200, loop=0)


    gif_buffer.seek(0)


    response = HttpResponse(gif_buffer.read(), content_type='image/gif')

    return render(request, 'generate_image.html', {'timestamp': int(time.time())})





def service(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        feedback = request.POST.get('service1')
        success_message = "Feedback sent successfully!"
        my_variable = request.session.get('my_variable', None)
        print("Feedback Recived From:",my_variable)
        print("Feedback:",feedback) 
        current_date = datetime.now().date()
        form = FeedbackForm()
        return render(request, 'service.html',{'feedback': feedback, 'current_date': current_date, 'my_variable': my_variable, 'form': form, 'success_message': success_message})
    else:
        form = FeedbackForm()
        return render(request, 'service.html', {'form': form})
    
    

def uniform_cleanliness(request):
    students = Student.objects.all()
    return render(request, 'uniform_cleanliness', {'students': students})

def guest(request):
    if request.method == 'POST':
        my_variable = request.POST.get("Logined as Guest")
        print(my_variable)
        return render(request, 'guest.html', {'my_variable': my_variable})
    else:
        return render(request, 'guest.html')







def restart_signup(request):

    request.session.pop('random_number', None)

    return redirect('signup.html')

def buisness(request):
        return render(request, 'buisness.html')



def hd_buyer(request):
        return render(request, 'hd_buyer.html')

def carpenter(request):
    name = request.POST.get('name')
    exp = request.POST.get('exp')
    skills = request.POST.get('skills')
    dor = request.POST.get('DOR')
    dob = request.POST.get('dob')
    address = request.POST.get('address')
    number = request.POST.get('number')
    completedProjects = request.POST.get('completedProjects')
    request.session['name'] = name
    request.session['exp'] = exp
    request.session['skills'] = skills
    request.session['dor'] = dor
    request.session['dob'] = dob
    request.session['address'] = address
    request.session['number'] = number
    request.session['completedProjects'] = completedProjects
    print("Carpenter form applied: ")
    print("Name: ", name)
    print("Experience: ", exp)
    print("Skills: ", skills)
    print("Date of registering: ", dor)
    print("Date of birth: ", dob)
    print("Address: ", address)
    print("Number: ", number)
    print("completedProjects: ", completedProjects)
    return render(request, 'carpenter.html')

def home_and_buisness(request):
         return render(request, 'home_and_buisness.html')

def home_buy(request):
         return render(request, 'home_buy.html')

         



def payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        name_on_card = request.POST.get('name_on_card')
        ccv = request.POST.get('ccv')
        card_brand = request.POST.get('card_brand')
        coupon_code = request.POST.get('coupon_code')
        phone_number = request.POST.get('phone_number')
        account_sid = 'AC221ca32b1a5350b9823cb32ceb6cecd6'
        auth_token = '239ebf18d85aa398dc3aa100704ea148'
        twilio_phone_number = '14155238886'
        receiver_phone_number = f'whatsapp:+91{phone_number}'
        client = Client(account_sid, auth_token)
        final_cost = float(request.POST['final_cost'])
        
        try:
            random_number = random.randint(1000, 1999)
            request.session['random_number'] = random_number
            otp_message = f"{final_cost} is credited for buying interiors in TechieHub"

            message = client.messages.create(
                body=otp_message,
                from_=f'whatsapp:{twilio_phone_number}',
                to=receiver_phone_number
            )
            print("Payment done for book")
            print("Final Cost:", final_cost)
            print("Card Number:", card_number)
            print("Phone Number:", phone_number)
            print("Name:", name_on_card)
            print("CCV:", ccv)
            print("Brand:", card_brand)
            print("Coupon:", coupon_code)
            return render(request, 'buisness.html')
        except TwilioRestException as e:
            error_message = str(e)
            if "is not a valid phone number" in error_message:
                error = 'Invalid phone number. Please enter a valid number.'
            else:
                print(f'Twilio API error: {error_message}')
                error = 'An error occurred while sending the message. Please try again.'
        return HttpResponseRedirect(reverse('buisness'))
    return render(request, 'payment.html')

def signup(request):
    if request.method == 'POST':
        account_sid = 'AC221ca32b1a5350b9823cb32ceb6cecd6'
        auth_token = '239ebf18d85aa398dc3aa100704ea148'
        twilio_phone_number = '14155238886'
        new_number = request.POST.get('new_number')
        receiver_phone_number = f'whatsapp:+91{new_number}'
        new_username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        new_gmail = request.POST.get('new_gmail')
        client = Client(account_sid, auth_token)

        try:
            random_number = random.randint(1000, 1999)
            request.session['random_number'] = random_number
            otp_message = f"Your OTP for Signing up in Techiehub is: {random_number}"
            

            message = client.messages.create(
                body=otp_message,
                from_=f'whatsapp:{twilio_phone_number}',
                to=receiver_phone_number
            )

            print("New Account Created ↓")
            print(f'OTP sent successfully!')
            print("OTP:", random_number)
            print("New Username - ", new_username)
            print("New Password - ", new_password)
            print("Gmail - ", new_gmail)
            print("Phone Number - ", new_number)
            
            return render(request, 'otp_verification.html', {'new_username': new_username, 'new_password': new_password, 'new_number': new_number, 'new_gmail': new_gmail})
        except TwilioRestException as e:

            error_message = str(e)
            if "is not a valid phone number" in error_message:
                error = 'Invalid phone number. Please enter a valid number.'
            else:

                print(f'Twilio API error: {error_message}')
                error = 'An error occurred while sending the message. Please try again.'

            return render(request, 'signup.html', {'error': error})
    else:
        return render(request, 'signup.html')

def forgot_password(request):
    if request.method == 'POST':
        account_sid = 'AC221ca32b1a5350b9823cb32ceb6cecd6'
        auth_token = '239ebf18d85aa398dc3aa100704ea148'
        twilio_phone_number = '14155238886'
        forgot_username = request.POST.get('forgot_username')
        forgot_password = request.POST.get('forgot_password')
        forgot_Gmail = request.POST.get('forgot_Gmail')
        forgot_number = request.POST.get('forgot_number')
        request.session['forgot_number'] = forgot_number
        receiver_phone_number  =f'whatsapp:+91{forgot_number}'
        client = Client(account_sid, auth_token)
        otp = random.randint(1000, 1999)
        request.session['otp'] = otp
        otp_message = f"Your OTP for Changing Password in Techiehub is: {otp}"
        message = client.messages.create(
            body=otp_message,
            from_=f'whatsapp:{twilio_phone_number}',
            to=receiver_phone_number
            )
        
        print("Changed Password ↓")
        print("Password changed for:", forgot_username)
        print("Gmail:", forgot_Gmail)
        print("Phone Number:", forgot_number)
        print("New Password: - ", forgot_password)
        return render(request, 'otp_password.html', {'forgot_password': forgot_password, 'forgot_username': forgot_username,'forgot_Gmail':forgot_Gmail,'forgot_number':forgot_number})
    else:
        error_message = 'Passwords do not match!'
    return render(request, 'forgot_password.html', {'error_message': error_message})

def about(request):
     return render(request, 'about.html')



def The_Starlight_Symphony_quiz(request):
     return render(request, 'The_Starlight_Symphony_quiz.html')


def The_enchanted_equinox(request):
     return render(request, 'The_enchanted_equinox.html')

def The_enchanted_equinox_quiz(request):
     return render(request, 'The_enchanted_equinox_quiz.html')


def The_Starlight_Symphony(request):
     return render(request, 'The_Starlight_Symphony.html')







def otp_password(request):
    if request.method == 'POST':    
        random_number = request.session.get('otp')
        entered_otp = request.POST.get('otp1')
        print(random_number)
        print(entered_otp)
        if entered_otp == str(random_number):
            success_message = 'Password Changed Sucessfully!'
            print(success_message)
            return render(request, 'otp_password.html', {'random_number': random_number, 'success_message': success_message})
        else:
            fail_message = 'Enter the correct OTP'
            print(fail_message)
        return render(request, 'otp_password.html', {'random_number': random_number, 'fail_message': fail_message})
    
    return render(request, 'otp_password.html')

    

def sample(request):
     return render(request, 'sample.html')


    


def contact(request):
    return render(request, 'contact.html')

def otp_verification(request):
    if request.method == 'POST':    
        random_number = request.session.get('random_number')
        entered_otp = request.POST.get('otp1')
        if entered_otp == str(random_number):
            success_message = 'Account created Sucessfully!'
            print(success_message)
            return render(request, 'otp_verification.html', {'random_number': random_number, 'success_message': success_message})
        else:
            fail_message = 'Enter the correct OTP'
            print(fail_message)
        return render(request, 'otp_verification.html', {'random_number': random_number, 'fail_message': fail_message})
    
    return render(request, 'otp_verification.html')

def loader(request):
    return render(request, 'loader.js')


def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = []

    product_id = int(product_id)
    if product_id not in request.session['cart']:
        request.session['cart'].append(product_id)
        request.session.modified = True

    return redirect('product_list')