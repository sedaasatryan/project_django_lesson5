from django.shortcuts import render, redirect
from .models import Notebook, Review
# Create your views here.
def home(request):
    notebook_list = Notebook.objects.all()
    return render(request, 'home.html', context = {
        'notebook_list':notebook_list
    })

def home_detail(request, id):
    one_not = Notebook.objects.get(pk=id)
    return render(request, 'home_detail.html', context = {
        'one_not':one_not
    })

def review(request):
    if request.method =="POST":
        new_email = request.POST.get('email')
        new_phone = request.POST.get('phone')
        new_text = request.POST.get('text')
        Review.objects.create(email=new_email, phone=new_phone, text = new_text)
        return redirect('home')
    return render(request, 'review.html')
