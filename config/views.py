# from django.contrib.auth import authenticate, login, logout
# from django.db import IntegrityError
from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.hashers import  check_password
# from django.views import View
# import json
from .models import *
# from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    foods = Food.objects.all()
    return render(request, 'index.html', {'foods':foods})

def about(request):
    return render(request, 'about.html')

# @login_required(login_url="login/")
def menu(request):
    foods = Food.objects.all()
    return render(request, 'menu.html', {'foods':foods})

# @login_required(login_url="/logout/")
def order(request):
    foods = Food.objects.all()
    return render(request, 'order.html', {'foods':foods})

def cart(request):
    return render(request, 'cart.html', {'cart' : cart})


# def login(request):
#     return render(request, 'login.html')

# def signup(request):
#     if  request.method == "POST":
#         f_name = request.POST.get('f_name')
#         l_name = request.POST.get('l_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         try:
#             signups = Login.objects.create(f_name=f_name, l_name=l_name, password=password, email=email, confirm_password=confirm_password)
#             if signups:
#                 return redirect(request, "signup.html", {"message": "?"})
#         except Exception as e:
#             print(e)
#     return render(request, 'signup.html')



def Contact(request):
    context={}
    if  request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        text = request.POST.get('text')
        
        comment = Comment(name=name, title=title, text=text, email=email)
        comment.save()
        context['text']=f"Dear {name}, Thanks for your time!"
        
    return render(request, 'contact.html', context)


def view(request, id):
    food = Food.objects.get(id=id)
    
    return render(request, 'detail.html', {'food':food})



def payment_done(request):
    pid = request.GET.get('PayerID')
    order_id = request.session.get('order_id')
    order_obj = Order.objects.get(id=order_id)
    order_obj.status=True 
    order_obj.payer_id = pid
    order_obj.save()

    return render(request, 'payment_successfull.html') 

def payment_cancel(request):
    ## remove comment to delete cancelled order
    # order_id = request.session.get('order_id')
    # Order.objects.get(id=order_id).delete()

    return render(request, 'payment_failed.html') 
