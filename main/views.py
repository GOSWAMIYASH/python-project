from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Submission

# Create your views here.

def index(request):
    dynamic_content = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'index.html', {'dynamic_content': dynamic_content})

def form_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Submission.objects.create(name=name, email=email)
        return redirect('data')
    return render(request, 'form.html')

def data_view(request):
    submissions = Submission.objects.all()
    return render(request, 'data.html', {'submissions': submissions})
