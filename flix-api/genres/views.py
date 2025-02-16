import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre

@csrf_exempt
def genre_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()

        data = [{'id': genre.id, 'name': genre.name} for genre in genres]

        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        if not request.body:
            return JsonResponse({'error': 'Empty request body'}, status=400)

        data = json.loads(request.body.decode('utf-8'))

        if not data.get("name"):
            return JsonResponse({
                'error': 'name is required'
            }, status=400)

        new_genre = Genre(name=data['name'])
        new_genre.save()

        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name}, 
            status=201
        )
