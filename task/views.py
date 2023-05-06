from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'task/home.html')

def add_task(request):
    return render(request, 'task/add_task.html')

def view_task(request):
    return render(request, 'task/view_task.html')

