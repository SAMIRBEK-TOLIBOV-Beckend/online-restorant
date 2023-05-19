from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def order(request):
    return render(request, 'order.html')

def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

# def register(request):
#     return render(request, 'contact.html')

def view(request):
    return render(request, 'detail.html')





# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "contact.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "contact.html")

# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("index"))

# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         fname = request.POST["firstname"]
#         lname = request.POST["lastname"]
#         profile = request.FILES.get("profile")
#         print(f"--------------------------Profile: {profile}----------------------------")
#         cover = request.FILES.get('cover')
#         print(f"--------------------------Cover: {cover}----------------------------")

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]   
#         if password != confirmation:
#             return render(request, "login.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.first_name = fname
#             user.last_name = lname
#             if profile is not None:
#                 user.profile_pic = profile
#             else:
#                 user.profile_pic = "profile_pic/no_pic.png"
#             user.cover = cover           
#             user.save()
#             Login.objects.create(user=user)
#         except IntegrityError:
#             return render(request, "login.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "login.html") 

# @csrf_exempt
# def like_post(request, id):
#     if request.user.is_authenticated:
#         if request.method == 'PUT':
#             post = Food.objects.get(pk=id)
#             print(post)
#             try:
#                 post.likers.add(request.user)
#                 post.save()
#                 return HttpResponse(status=204)
#             except Exception as e:
#                 return HttpResponse(e)
#         else:
#             return HttpResponse("Method must be 'PUT'")
#     else:
#         return HttpResponseRedirect(reverse('login'))

# @csrf_exempt
# def unlike_post(request, id):
#     if request.user.is_authenticated:
#         if request.method == 'PUT':
#             post = Food.objects.get(pk=id)
#             print(post)
#             try:
#                 post.likers.remove(request.user)
#                 post.save()
#                 return HttpResponse(status=204)
#             except Exception as e:
#                 return HttpResponse(e)
#         else:
#             return HttpResponse("Method must be 'PUT'")
#     else:
#         return HttpResponseRedirect(reverse('login'))


# @csrf_exempt
# def comment(request, post_id):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             data = json.loads(request.body)
#             comment = data.get('comment_text')
#             post = Food.objects.get(id=post_id)
#             try:
#                 newcomment = Food.objects.create(post=post,commenter=request.user,comment_content=comment)
#                 post.comment_count += 1
#                 post.save()
#                 print(newcomment.serialize())
#                 return JsonResponse([newcomment.serialize()], safe=False, status=201)
#             except Exception as e:
#                 return HttpResponse(e)
    
#         post = Food.objects.get(id=post_id)
#         comments = Order.objects.filter(post=post)
#         comments = comments.order_by('-comment_time').all()
#         return JsonResponse([comment.serialize() for comment in comments], safe=False)
#     else:
#         return HttpResponseRedirect(reverse('login'))
