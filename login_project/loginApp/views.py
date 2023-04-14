from django.shortcuts import render
from collections.abc import Mapping
import pyrebase

# Create your views here.

config = {
    'apiKey': "AIzaSyDERRjbrRYvHSXG8zbQvbH18ZXBHd-CpIc",
    'authDomain': "loginregisterauth-4c7e6.firebaseapp.com",
    'projectId': "loginregisterauth-4c7e6",
    'storageBucket': "loginregisterauth-4c7e6.appspot.com",
    'messagingSenderId': "159495611742",
    'appId': "1:159495611742:web:fba4365f0705b248e2dbcf",
    'measurementId': "G-MQRBMT5B00",
    'databaseURL': ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def login(request):
    return render(request, 'login.html')

def postlogin(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email, passw)
    except:
        message = "Invalid Credentials"
        return render(request, 'login.html', {"messages": message})
    print(user)
    context={
        'email':email
    }
    return render(request, 'welcome.html', context)

