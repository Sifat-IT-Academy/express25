from django.shortcuts import render
from django.views import View
from store.models import Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
import json



class StoreDetailView(View):

    def get(self, request, id):
        store = Category.objects.get(id=id,category_type='Store')
        json_response = {
            'name':store.name,
            'address':{'city':store.address.city,
                       'district':store.address.district},
            'description':store.description,
            'phone_number':store.phone_number,
            'rating':store.rating
        }
        return JsonResponse(json_response)
    
    #delete, put, patch


    
class StoreListAPIView(View):
    def get(self, request):
        stores = Category.objects.filter(category_type='Store')
        json_responses = list()
        for store in stores:
            json_response = {
                'name':store.name,
                'address':{'city':store.address.city,
                        'district':store.address.district},
                'description':store.description,
                'phone_number':store.phone_number,
                'rating':store.rating
            }
            json_responses.append(json_response)


        return JsonResponse(json_responses,safe=False)
    
    #post
    
#postman

class StoreDeleteView(View):
    
    def delete(self, request, id):
        store = get_object_or_404(Category, Q(id=id) & Q(category_type='Store'))
        store_name = self.name
        store.delete()
        json_response = {
            'message': f'Store "{store_name}" has been successfully deleted.'
        }
        return JsonResponse(json_response, status=200)
    

class StoreUpdateView(View):
    def put(self, request, id):
        store = get_object_or_404(Category, Q(id=id) & Q(category_type='Store'))
        data = json.loads(request.body)

        if 'name' in data:
            store.name = data['name']
        if 'description' in data:
            store.description = data['description']
        if 'phone_number' in data:
            store.phone_number = data['phone_number']
        if 'rating' in data:
            store.rating = data['rating']
        if 'address' in data:
            if 'city' in data['address']:
                store.address.city = data['address']['city']
            if 'district' in data['address']:
                store.address.district = data['address']['district']

                store.save()
        
        json_response = {
            'message': f'Store "{store.name}" has been successfully updated.'
        }
        
        return JsonResponse(json_response, status=200)
    
class StorePartialUpdateView(View):

    def patch(self, request, id):
        store = get_object_or_404(Category, Q(id=id) & Q(category_type='Store'))

        data = json.loads(request.body)
        
        if 'name' in data:
            store.name = data['name']
        if 'description' in data:
            store.description = data['description']
        if 'phone_number' in data:
            store.phone_number = data['phone_number']
        if 'rating' in data:
            store.rating = data['rating']
        if 'address' in data:
            if 'city' in data['address']:
                store.address.city = data['address']['city']
            if 'district' in data['address']:
                store.address.district = data['address']['district']

        store.save()
        
        json_response = {
            'message': f'Store "{store.name}" has been partially updated.'
        }
        
        return JsonResponse(json_response, status=200)