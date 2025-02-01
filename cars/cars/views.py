from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__contains=search)
    
    return render(
        request,
        'cars.html',
        { 'cars': cars }
    )

def new_car_view(request):
    return render(
        request,
        'new_car.html'
    )