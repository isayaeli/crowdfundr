from django.core.exceptions import PermissionDenied
from functools import wraps
from django.contrib.auth.models import User
from django.shortcuts import redirect

def donor_required(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.user_type == 'donor': 
            return view(request, *args, **kwargs)
        return redirect('donor_confirm')
    return _view


def sme_required(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.user_type == 'sme': 
            return view(request, *args, **kwargs)
        return redirect('sme_confirm')
    return _view



def active_required(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.profile.is_active == True: 
            return view(request, *args, **kwargs)
        return redirect('confirm')
    return _view