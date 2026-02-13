from django.shortcuts import render,redirect
from .models import Services
from .forms import ServicesForm 

# Create your views here.
def servicesList(request):
    services = Services.objects.all()
    return render(request, 'services/servicesList.html', {"services": services})

def createServices(request):
    if (request.method == "POST"):
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serviceList')
    else:
        form = ServicesForm()
        return render(request, 'services/createServicesForm.html', {"form": form})
    

def deleteService(request, id):
    Services.objects.filter(id=id).delete()
    return redirect('serviceList')

def updateService(request, id):
    service = Services.objects.get(id=id)
    if request.method == "POST":
        form = ServicesForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('serviceList')
    else:
        form = ServicesForm(instance=service)
        return render(request, 'services/updateServicesForm.html', {"form": form})