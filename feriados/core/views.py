import datetime
from django.http import HttpResponse
from django.shortcuts import render

date = datetime.date.today()

def natal(request):
    if date.day == 25 and date.month == 12:
        contexto = {'natal': True}
        return render(request, 'natal.html', contexto)
    else:
        contexto = {'natal': False} 
        return render(request, 'natal.html', contexto)

def tiradentes(request):
    if date.day == 21 and date.month == 4:
        contexto = {'tiradentes': True}
        return render(request, 'tiradentes.html', contexto)
    else:
        contexto = {'tiradentes': False}
        return render(request, 'tiradentes.html', contexto)

def orlando(request):
    if date.strftime("%A") == 'Wednesday':
        contexto = {'orlando': True}
        return render(request, 'orlando.html', contexto)
    else:
        contexto = {'oralndo': False}
        return render(request, 'orlando.html', contexto)

