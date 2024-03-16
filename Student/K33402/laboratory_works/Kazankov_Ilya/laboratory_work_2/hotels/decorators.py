from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else: 
            return view_func(request, *args, **kwargs)
    return wrapper