from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                messages.success(request, 'Connexion réussie')
                return redirect('administrateur')
            if user.groups.filter(name='Ccco').exists():
                messages.success(request, 'Connexion réussie')
                return redirect('importer')
            if user.groups.filter(name='Dpf').exists():
                messages.success(request, 'Connexion réussie')
                return redirect('dpf')
            else:
                return redirect('agent')
        else:
            messages.error(request, 'Mot de passe incorrect ou nom utilisateur incorrect')  # Message d'erreur en cas de mot de passe incorrect
        return redirect('login')
    return render(request, 'account/login.html')

@login_required
def logout(request):
    return redirect('/')