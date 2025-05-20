from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .forms import RegisterForm, AvatarUploadForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import User

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

def account_detail(request, pk):
    user = User.objects.get(id=pk)
    is_owner = request.user.is_authenticated and request.user.pk == user.pk
    return render(request, 'accounts/profile_detail.html', {
        'user': user,
        'is_owner': is_owner,
    })


@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect(f'/detail/{request.user.pk}/')
    return HttpResponseForbidden("Недопустимий запит")