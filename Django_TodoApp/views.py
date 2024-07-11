from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import Todo


# Create your views here.
def HomePage(request):
    obj = Todo.objects.all(),
    template_name = 'Django_TodoApp/Todo.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def TodoFormView(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'Django_TodoApp/Todo.html'
    context = {'form': form}
    return render(request, template_name, context)


def showView(request):
    obj = Todo.objects.all(),
    template_name = 'Django_TodoApp/showTasks.html'
    context = {'obj': obj}
    return render(request, template_name, context)


def updateView(request, currentId):
    obj = Todo.objects.get(id == currentId),
    form = TodoForm(instance=obj)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'Django_TodoApp/Todo.html'
    context = {'form': form}
    return render(request, template_name, context)


def deleteView(request, currentId):
    obj = Todo.objects.get(id == currentId),
    if request.method == 'POST':
        obj.delete()
        return redirect('show')
    template_name = 'Django_TodoApp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)


# INSTALLED_APPS = [
#     # ...
#     'crispy_forms',
#     'crispy_bootstrap5',
# ]
#
# CRISPY_TEMPLATE_PACK = 'bootstrap5'