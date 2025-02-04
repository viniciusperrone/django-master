from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from django.conf import settings

from cars.models import Car, CarInventory

import google.generativeai as genai 

genai.configure(api_key=settings.API_KEY) 

def car_gemini_ai(model, brand, year): 
    message = ''' Elaborar um resumo sobre o carro {} da marca {} do ano {} com 200 caracteres. ''' 
    message = message.format(model, brand, year) 
    model = genai.GenerativeModel("gemini-1.5-flash") 
    response = model.generate_content( 
        message, 
        generation_config = genai.GenerationConfig(max_output_tokens=300,) 
    ) 
    
    return response.text

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = car_gemini_ai(instance.model, instance.brand, instance.model_year)
        
        print(instance.bio)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()