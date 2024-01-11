from django.shortcuts import render, redirect
from .models import Zapis
from .forms import ZapisForm
from .models import Vrahi

def zapis (request):
    zapis = Zapis.objects.all()
    return render(request, 'bd/zapis.html', {'zapis' : zapis})

def vrachi (request):
    vrach= Vrahi.objects.all()
    return render(request, 'bd/vrach.html', {'vrach': vrach})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ZapisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'
    form = ZapisForm()
    data = {
        'form' : form,
        'error' : error,
    }
    return render(request, 'bd/createZap.html', data)


