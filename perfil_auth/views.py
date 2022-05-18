from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, "perfil_auth/index.html")

def perfil(request):
	return render(request, "perfil_auth/perfil.html")

def entrar(request):
	return render(request, "registration/login.html")