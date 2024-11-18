from django.shortcuts import render, redirect
from .forms import ContactFormModel, ReviewFormModel
from .models import *

def index(request):
    reviews = Review.objects.filter(on_list=True)
    context = {
        'reviews': reviews
    }
    return render(request, 'core/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = ContactFormModel()
        

    context = {
        'fm':form
    }

    return render(request, 'core/contact.html', context)


def review(request):
    if request.method =='POST':
        form = ReviewFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = ReviewFormModel()
    context={
        'fm':form
    }
    return render(request, 'core/review.html', context)