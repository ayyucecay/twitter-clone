# Main Imports

# Django Imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from .models import Profile, Tweet

def profile(request, id):
    """
    In this view the users can see the profile page of the website which
    holds a profile information and posted tweet
    """
    try:
        profile_info = Profile.objects.get(id=id)
    except ObjectDoesNotExist:
        profile_info = None


    # Getting all of the tweet to list and display them
    try:
        all_tweets = Tweet.objects.all().order_by("-id")
    except ObjectDoesNotExist:
        all_tweets = None





    data = {
        'profile_info': profile_info,
        'all_tweets': all_tweets,
    }


    return render(request, 'profile.html', data)
