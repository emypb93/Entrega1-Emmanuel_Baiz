from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
""" def inicio(request):
    return render(request, 'index.html') """

def libro(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html',{'autor_form': autor_form})
