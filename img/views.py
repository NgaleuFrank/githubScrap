from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .models import *


def index(request):
    if request.method == 'POST':
        github_user = request.POST['github_user']
        user = request.POST['user']
        url = 'https://github.com/' + github_user  # the github link and user name github
        r = requests.get(url)  # get the url link (Read)
        soup = BeautifulSoup(r.content)  # get the content
        profile = soup.find('img', {'alt': 'Avatar'})['src']  # find the user profile image
        # print(profile)  # for img in profile:  #     print(img['src'])

        new_github = Github(
            githubuser=github_user,
            image_link=profile,
            user_name=user
        )
        new_github.save()   # save the new github information (github_user and image ) into data base
        messages.info(request, 'User ' + github_user + '    Image Saved')
        return redirect('/')

    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exist')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                User.save(user)
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def images(request):
    user_name = request.user
    git_hub = Github.objects.filter(user_name=user_name)
    return render(request, 'images.html', {'git_hub': git_hub})
