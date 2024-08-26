from django.shortcuts import render
from .models import Todo

# Create your views here.


def index(request):
    context = {
        'alltodos': Todo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)
