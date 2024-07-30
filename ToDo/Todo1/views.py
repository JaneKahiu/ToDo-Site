from django.shortcuts import render,redirect
from django.http import HttpResponse  
from .models import ToDo
from .forms import ToDoForm  
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def todolist(request):
    item_list = ToDo.objects.order_by("-created_date")
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    else:
        form = ToDoForm()

    page = {
        'form': form,
        'list': item_list,
        'title': 'TODO LIST',
    }
    return render(request, 'todolist.html', page)

def remove(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todolist')