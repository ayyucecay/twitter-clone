# Main Imports

# Django Imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from .models import TopicsFollow
from profile_page.models import Tweet


def main_page(request):
    """
    In this view the users can see the home page of the website which
    holds a they can see tweets posted by other people
    """
    try:
        topics = TopicsFollow.objects.all()
    except ObjectDoesNotExist:
        topics = None


    # Getting all of the tweet to list and display them
    try:
        all_tweets = Tweet.objects.all().order_by("-id")
    except ObjectDoesNotExist:
        all_tweets = None

    data = {
        'topics': topics,
        'all_tweets': all_tweets,
    }


    return render(request, 'homeapp.html', data)
