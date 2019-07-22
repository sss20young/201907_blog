from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user) # 회원가입 후 자동 로그인
            return redirect('show')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST': 
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password) # 등록된 회원인지 확인
        if user is not None:
	        auth.login(request, user) # 로그인
	        return redirect('show')
        else:
	        return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
      
def logout(request):
    if request.method == 'POST': 
        auth.logout(request) # 로그아웃
        return redirect('home')
    return render(request, 'login.html')