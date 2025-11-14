from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins

# Create your views here.


#region function base view

@api_view(["GET", "POST"])
def all_todos(request: Request):
    if request.method == "GET":
        todos = ToDo.objects.order_by("priority").all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(request: Request, todo_id: int):
    # todo = ToDo.objects.filter(pk=todo_id).first()
    try:
        todo = ToDo.objects.get(pk=todo_id)
    except ToDo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

#endregion

#region class base view

class TodosListApiViews(APIView):
    def get(self, request: Request):
        todos = ToDo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)
        

class TodosDetailApiView(APIView):    
    @property
    def todo(self):
        todo_id = self.kwargs.get('todo_id')
        return get_object_or_404(ToDo, pk=todo_id)

    def get(self, request: Request,*args,**kwargs):
        serializer = TodoSerializer(self.todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, *args, **kwargs):
        serializer = TodoSerializer(self.todo, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, *args, **kwargs):
        self.todo.delete()
        return Response(status.HTTP_204_NO_CONTENT)


#endregion

#region mixins

class TodosListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ToDo.objects.order_by('priority').all()
    serializer_class = TodoSerializer   

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodosDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ToDo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request: Request, pk):
        return self.update(request, pk)
    
    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

#endregion
