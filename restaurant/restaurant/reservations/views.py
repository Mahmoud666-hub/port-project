from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESERVATIONS_FILE = os.path.join(BASE_DIR, 'reservations.json')

@csrf_exempt
def make_reservation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        persons = data.get('persons')
        date = data.get('date')
        time = data.get('time')
        
        reservation = {
            'name': name,
            'email': email,
            'persons': persons,
            'date': date,
            'time': time
        }
        
        if os.path.exists(RESERVATIONS_FILE):
            with open(RESERVATIONS_FILE, 'r+') as file:
                reservations = json.load(file)
                reservations.append(reservation)
                file.seek(0)
                json.dump(reservations, file, indent=4)
        else:
            with open(RESERVATIONS_FILE, 'w') as file:
                json.dump([reservation], file, indent=4)
        
        return JsonResponse({'status': 'success', 'message': 'Reservation made successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def home(request):
    return render(request, 'reservations/home.html')