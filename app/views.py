# views.py
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Doctor 
from django.forms.models import model_to_dict
def index(request):
    return render(request, 'index.html')



def search_doctors(request):
    if request.method == 'GET':
        specialization = request.GET.get('specialization', '')
        location = request.GET.get('location', '')

        # Filter doctors based on specialization and location
        doctors = Doctor.objects.filter(specialization__icontains=specialization, location__icontains=location)

        # Serialize the data, converting ImageFieldFile to image URL
        serialized_doctors = [
            {
                'name': doctor.name,
                'specialization': doctor.specialization,
                'location': doctor.location,
                'phone': doctor.phone,
                'email': doctor.email,
                'image': doctor.image.url if doctor.image else '',
            }
            for doctor in doctors
        ]

        return JsonResponse(serialized_doctors, safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
