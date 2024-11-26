from django.shortcuts import render
from .forms import DoccumentForm
from .models import Doccument
# Create your views here.
def upload_files(request):
    if request.method == 'POST':
        form = DoccumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else :
        form = DoccumentForm()
    doccuments = Doccument.objects.all()
    return render(request,'upload.html',{'form':form , 'doccuments':doccuments})