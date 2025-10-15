from django.shortcuts import render
from todo.models import ToDo
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


def index_page(request):    
    context = {
        'todos': ToDo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)


@api_view(['GET'])
def todos_json(request: Request):
    todos = list(ToDo.objects.order_by('priority').all().values('title', 'is_done'))
    return Response({'todos': todos}, status.HTTP_200_OK)


# def todos_json(request: HttpRequest):
#     todos = list(ToDo.objects.order_by('priority').all().values('title', 'is_done'))
#     return JsonResponse({'todos': todos})
