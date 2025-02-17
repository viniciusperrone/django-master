import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from genres.models import Genre

HTTP_METHODS = (
    ('GET', 'GET'), 
    ('PUT', 'PUT'), 
    ('POST', 'POST'), 
    ('DELETE', 'DELETE'),
)

@csrf_exempt
def create_and_list_genre_view(request):
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
    
@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}

        return JsonResponse(data, safe=False)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))

        genre.name = data['name']

        genre.save()

        return JsonResponse({'id': genre.id, 'name': genre.name}, status=203)

    elif request.method == 'DELETE':
        genre.delete()

        return JsonResponse({'message': 'Successfully deleted genre'}, status=204)