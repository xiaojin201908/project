from django.http import HttpResponse
from .models import Pet
from django.shortcuts import render
def all_pets(request):
    text = ''
    pets = Pet.objects.all()
    context = {
            'pets': pets,
            }
    
    return render(request, 'adopt/all.html', context)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id = pet_id)
    return HttpResponse(pet.name)
