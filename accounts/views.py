from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def auth_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/')

    return render(request, 'accounts/auth.html')