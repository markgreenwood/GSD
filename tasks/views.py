from django.shortcuts import redirect, render
from tasks.models import Task 

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Task.objects.create(text=request.POST['task_text'])
        return redirect('/tasks/the-only-list-in-the-world/')

    tasks = Task.objects.all()
    return render(request, 'home.html')

def view_list(request):
    tasks = Task.objects.all()
    return render(request, 'list.html', {'tasks': tasks})
