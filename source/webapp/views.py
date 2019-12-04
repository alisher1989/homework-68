import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def Index(request):
    return render(request, 'index.html')


def is_valid(A, B):
    if not A or not B:
        return False, 'Data should contain two numbers named A and B.'
    if type(A) not in (int, float) or type(B) not in (int, float):
        return False, 'Both A and B should be numbers'
    return True, None


def make_response(data, status=200):
    response = JsonResponse(data)
    response.status_code = status
    return response


@csrf_exempt
def add(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            return JsonResponse({'answer': A + B})
        else:
            return make_response({'error': 'No data provided'}, 400)
    return make_response({'error': 'Method not allowed'}, 405)


@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            return JsonResponse({'answer': A - B})
        else:
            return make_response({'error': 'No data provided'}, 400)
    return make_response({'error': 'Method not allowed'}, 405)


@csrf_exempt
def multiply(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            return JsonResponse({'answer': A * B})
        else:
            return make_response({'error': 'No data provided'}, 400)
    return make_response({'error': 'Method not allowed'}, 405)


@csrf_exempt
def divide(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            return JsonResponse({'answer': A / B})
        else:
            return make_response({'error': 'No data provided'}, 400)
    return make_response({'error': 'Method not allowed'}, 405)
