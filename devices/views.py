# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.forms import UserCreationForm
# from .models import Device

# # Verifica se o usuário é superusuário
# def is_superuser(user):
#     return user.is_superuser

# # Página de Login
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect("device_list")
#         else:
#             return render(request, "devices/login.html", {"error": "Credenciais inválidas."})
#     return render(request, "devices/login.html")

# # Logout
# def logout_view(request):
#     logout(request)
#     return redirect("login")

# # Lista os dispositivos cadastrados pelo usuário logado
# @login_required
# def device_list(request):
#     devices = Device.objects.filter(user=request.user)
#     return render(request, "devices/device_list.html", {"devices": devices})

# # Página de cadastro de dispositivo
# @login_required
# def register_device(request):
#     if request.method == "POST":
#         device_type = request.POST.get("device_type")
#         model = request.POST.get("model")
#         device_id = request.POST.get("device_id")
#         odm = request.POST.get("odm")

#         # Criar e salvar o dispositivo
#         Device.objects.create(
#             device_type=device_type,
#             model=model,
#             device_id=device_id,
#             odm=odm,
#             user=request.user
#         )
#         return redirect("device_list")
    
#     return render(request, "devices/register_device.html")

# # Página de cadastro de usuário (apenas para superusuários)
# @login_required
# @user_passes_test(is_superuser)
# def register_user(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # Cria o usuário
#             user = form.save()
#             login(request, user)  # Faz o login do usuário automaticamente após o cadastro
#             return redirect("device_list")  # Redireciona para a lista de dispositivos
#     else:
#         form = UserCreationForm()  # Se o método não for POST, exibe um formulário vazio

#     return render(request, "devices/register_user.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Device
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
# Verifica se o usuário é superusuário
def is_superuser(user):
    return user.is_superuser

# Página de Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("device_list")
        else:
            return render(request, "devices/login.html", {"error": "Credenciais inválidas."})
    return render(request, "devices/login.html")

# Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Lista os dispositivos cadastrados pelo usuário logado
@login_required
def device_list(request):
    devices = Device.objects.all()  # Busca todos os dispositivos do banco de dados
    return render(request, "devices/device_list.html", {"devices": devices})


# Página de cadastro de dispositivo
@login_required
def register_device(request):
    if request.method == "POST":
        device_type = request.POST.get("device_type")
        model = request.POST.get("model")
        device_id = request.POST.get("device_id")
        odm = request.POST.get("odm")

        # Criar e salvar o dispositivo
        Device.objects.create(
            device_type=device_type,
            model=model,
            device_id=device_id,
            odm=odm,
            user=request.user
        )
        return redirect("device_list")
    
    return render(request, "devices/register_device.html")

# Página de cadastro de usuário (apenas para superusuários)
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Verifica se o email contém "positivo.com.br"
        if not email.endswith("@positivo.com.br"):
            return render(request, "devices/register_user.html", {"error": "O email deve ser do domínio positivo.com.br!"})

        # Confirmação de senha
        if password1 != password2:
            return render(request, "devices/register_user.html", {"error": "As senhas não coincidem!"})

        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            return render(request, "devices/register_user.html", {"error": "Usuário já existe!"})

        # Verifica se o email já está cadastrado
        if User.objects.filter(email=email).exists():
            return render(request, "devices/register_user.html", {"error": "Email já cadastrado!"})

        # Criação do usuário
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect("login")  # Redireciona para o login após cadastro

    return render(request, "devices/register_user.html")



