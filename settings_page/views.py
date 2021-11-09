# Main Imports

# Django Imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from profile_page.models import Profile


def update_profile(request, id):
    """
    users change own profile settings
    """

    try:
        profile_info = Profile.objects.get(id=id)
    except ObjectDoesNotExist:
        profile_info = None

    if request.POST.get("profile_settings_submit"):
        profile_photo = request.POST.get("profile_photo")
        banner_photo = request.POST.get("banner_photo")
        full_name = request.POST.get("full_name")
        bio = request.POST.get("bio")




    data= {
        'profile_info': profile_info,
    }

    return render(request, 'settings.html', data)
