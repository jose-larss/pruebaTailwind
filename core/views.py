from django.shortcuts import render

from .models import Banderas

def indice(request):
    banderas = Banderas.objects.all()
    return render(request, "core/indice.html", {"banderas":banderas})
