from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .forms import RegisterForm

def auth_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'accounts/auth.html')
def register_form(request):
    if not request.user.is_authenticated or request.user.role != "teacher":
        return redirect('/')
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:          
        form=RegisterForm()
    return render(
        request, 'accounts/register_form.html',
        {'form': form}
    )
def logout_view(request):
    logout(request)
    return redirect('/')