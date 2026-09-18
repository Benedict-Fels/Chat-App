from django.shortcuts import render

import json
from django.http import JsonResponse
from .models import Contact  

def chat_view(request):
    if request.method == 'GET':
        contacts = list(Contact.objects.values())
        return JsonResponse(contacts, safe=False, status=200)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_entry = Contact.objects.create(
                name=data.get('name'),
                message=data.get('message')
            )
            return JsonResponse({
                'status': 'success',
                'id': new_entry.id
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)