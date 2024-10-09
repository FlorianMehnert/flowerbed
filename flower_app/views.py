from django.shortcuts import render, redirect
from .models import Flower
from .forms import FlowerForm
from django.utils import timezone


def add(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()  # Save the flower to the database
            return redirect('show')  # Redirect to the flower list after saving
    else:
        form = FlowerForm()
    return render(request, 'flower_app/add.html', {'form': form})


def show(request):
    flowers = Flower.objects.all()  # Get all flowers from the database
    return render(request, 'flower_app/show.html', {'flowers': flowers})
