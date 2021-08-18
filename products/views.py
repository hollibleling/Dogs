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

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog = Dog.objects.create(
            name=data['dog'],
            owner=Owner.objects.get(name=data['owner']),
            age=data['dog_age'],
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)