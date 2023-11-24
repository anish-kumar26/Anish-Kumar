from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.conf.urls.static import static
import base64
import os
from django.views.generic import ListView
import time
import js2py
import webview
import threading
from django.views import View
from django.http import HttpResponse
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Product, Order, OrderStatus
def home(request):
    # Add logic to calculate estimated delivery time
    return render(request, 'home.html')

def product_page(request, product_type):
    products = Product.objects.filter(...)  # Filter products based on type
    return render(request, f'{product_type}.html', {'products': products})

def cart(request):
    # Filter orders for the current user
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
        # Handle the form submission here
        from_email = request.POST.get('from_email')
        to_email = request.POST.get('to_email')
        message = request.POST.get('message')

        # Implement your logic to send the email using the Gmail API or any other method

        # For now, set a success message
        success_message = "Email sent successfully!"

        return render(request, self.template_name, {'success_message': success_message})


def show_loading_screen():
    html_content = """
    <html>
    <head>
        <style>
            #loadingScreen {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
            }

            #content {
                display: none;
            }
        </style>
    </head>
    <body>
        <div id="loadingScreen">
            <p>Loading...</p>
        </div>
        <div id="content">
            <p>Your content goes here!</p>
        </div>
        <script>
            document.addEventListener('DOMContentLoaded', function () {
                var loadingScreen = document.getElementById('loadingScreen');
                var content = document.getElementById('content');

                // Show loading screen
                loadingScreen.style.display = 'flex';

                // Simulate loading (replace this with actual AJAX calls)
                setTimeout(function () {
                    // Hide loading screen after a delay (simulating content loading)
                    loadingScreen.style.display = 'none';
                    // Show content
                    content.style.display = 'block';
                }, 2000); // Replace 2000 with the actual time your content takes to load
            });
        </script>
    </body>
    </html>
    """

    webview.create_window("techiehub", html=html_content, width=800, height=600)

if __name__ == '__main__':
    # Run the webview in a separate thread
    threading.Thread(target=show_loading_screen).start()

    # Keep the Python script running
    webview.start()

def home(request):
    return render(request, 'Techiehub/home.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'anishtechie20@gmail.com' and password == 'welcome0@123':
            my_variable = "Welcome to Techiehub, Anish"

            return render(request, 'techiehub/home.html', {'my_variable': my_variable})

        elif username == 'chellakannan83@gmail.com' and password == 'Welcome0!':
            my_variable = "Welcome to Techiehub, Chella"

            return render(request, 'techiehub/home.html', {'my_variable': my_variable})
            
        elif username == 'subhakrishnan84@gmail.com' and password == 'anish@123456':
            my_variable = "Welcome to Techiehub, Subha"    

            return render(request, 'techiehub/home.html', {'my_variable': my_variable})
        
        elif username == 'subhakrishnan84@gmail.com' and password == 'anish@123456':
            return render(request, 'techiehub/home.html')  # You might want to change the template here
        # Check the third set of credentials
        elif username == 'chellakannan83@gmail.com' and password == 'Welcome0!':
            return render(request, 'techiehub/home.html')  # You might want to change the template here
        
        elif username == 'anishtechie20@gmail.com' and password == 'welcome0@123':
            return render(request, 'techiehub/home.html')

        else:
            error_message = 'Enter the correct username and password.'
            return render(request, 'login.html', {'error_message': error_message})


    return render(request, 'login.html')


# views.py

def service(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        print(f"Received POST request. service: {service}")

        # Assuming you have a feedback field in your form
        service = request.POST.get('service')
        print(f"Feedback received: {service}")

        # You can process the feedback further if needed
        # For example, you could save it to a database

        # Redirect to the home view
        return redirect('service.html')

    return render(request, 'Techiehub/service.html')

    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def loader(request):
    return render(request, 'loader.js')