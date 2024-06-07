from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import UploadedImage

def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadImageForm()
    images = UploadedImage.objects.all()
    return render(request, 'index.html', {'form': form, 'images': images})