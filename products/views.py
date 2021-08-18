from django.shortcuts import render

# Create your views here.

import json

from django.http     import JsonResponse
from django.views    import View

from products.models import Owner, Dog

class SampleView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name=data['owner'],
            email=data['email'], 
            age=data['age'], 
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        results2 = []
        for dog in dogs:
            results.append(
                {
                    "owner_name" : dog.owner.name, 
                    "email" : dog.owner.email,
                    "owner_age" : dog.owner.age,
                    "dog_name" : dog.name,
                    "dog_age" : dog.age
                }
            )
        for dog in dogs:
            results2.append(
                {
                    "owner_name" : dog.owner.name, 
                    "email" : dog.owner.email,
                    "owner_age" : dog.owner.age,
                }
            )
        return JsonResponse({'results':results, 'results2':results2}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog = Dog.objects.create(
            name=data['dog'],
            owner=Owner.objects.get(name=data['owner']),
            age=data['dog_age'],
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    "dog_name" : dog.name,
                    "owner" : dog.owner.name, 
                    "dog_age" : dog.age
                }
            )
        return JsonResponse({'resutls':results}, status=200)
