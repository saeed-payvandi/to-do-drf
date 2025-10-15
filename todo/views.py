from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def all_todos(request: Request):
    todos = ToDo.objects.order_by('priority').all()
    todo_serializer = TodoSerializer(todos, many=True)
    return Response(todo_serializer.data, status.HTTP_200_OK)