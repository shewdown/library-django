from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.cache import cache



def main(request):
    return render(request, 'main/main.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def favorites(request):
    return render(request, 'main/favorites.html')

def news(request):
    return render(request, 'main/news.html')

def support(request):
    return render(request, 'main/support.html')

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Логин занят')
            return render(request, 'profile/reg.html')

        if password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return render(request, 'profile/reg.html')


        user = User.objects.create_user(
            username=username,
            password=password1
        )
        user.save()

        user = authenticate(request, username=username, password=password1)
        login(request, user)
        return redirect('profile')

    return render(request, 'profile/reg.html')

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Неверный логин или пароль ')
            return render(request, 'profile/log.html')

    return render(request, 'profile/log.html')

@login_required
def profile(request):
    return render(request, 'profile/profile.html', {
        'username': request.user.username,
        'is_authenticated': True  # Явное указание статуса
    })

def full_logout(request):
    cache.clear()                          # Удаляем данные из кеша
    logout(request)                        # Выход из системы
    request.session.flush()                # Очистка сессии
    response = redirect('main')
    response.delete_cookie('sessionid')    # Удаление всех связанных куков
    response.delete_cookie('csrftoken')
    return response