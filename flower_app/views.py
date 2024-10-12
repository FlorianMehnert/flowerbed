from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Flower
from .forms import FlowerForm
from django.utils import timezone


def add(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()  # Save the flower to the database
            return redirect('add')  # Redirect to the flower list after saving
    else:
        form = FlowerForm()
        flowers = Flower.objects.all()  # Get all flowers from the database
        return render(request, 'flower_app/add.html', {'form': form, 'flowers': flowers})
    return render(request, 'flower_app/add.html', {'form': form})

def delete_flower(request, flower_id):
    if request.method == 'POST':
        try:
            flower = Flower.objects.get(id=flower_id)
            flower.delete()
            return JsonResponse({'status': 'success'})
        except Flower.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Flower not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)



def show(request):
    flowers = Flower.objects.all()  # Get all flowers from the database
    return render(request, 'flower_app/show.html', {'flowers': flowers})
