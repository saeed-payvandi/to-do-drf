from django.shortcuts import render
from todo.models import ToDo

# Create your views here.


def index_page(request):    
    context = {
        'todos': ToDo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)