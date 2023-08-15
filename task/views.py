from django.shortcuts import redirect, render

from task.forms import TaskStoreForm
from task.models import TaskStoreModel


def show_tasks(request):
    tasks = TaskStoreModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        task = TaskStoreForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('show_tasks')
    else:
        tasks = TaskStoreModel.objects.all()
        form = TaskStoreForm()
        return render(request, 'add_task.html', {'form': form, 'tasks': tasks})


def delete_task(request, id):
    task = TaskStoreModel.objects.get(pk=id).delete()
    return redirect('show_tasks')


def edit_task(request, id):
    if request.method == "POST":
        task = TaskStoreModel.objects.get(pk=id)
        updated_task = TaskStoreForm(request.POST)
        if updated_task.is_valid():
            task.task = updated_task.cleaned_data['task']
            task.detail = updated_task.cleaned_data['detail']
            task.save()
            return redirect('show_tasks')
    else:
        tasks = TaskStoreModel.objects.all()
        task = TaskStoreModel.objects.get(pk=id)
        form = TaskStoreForm(instance=task)
        return render(request, 'add_task.html', {'form': form, 'tasks': tasks})


def completed_task(request):
    tasks = TaskStoreModel.objects.all()
    return render(request, 'completed_task.html', {'tasks': tasks})


def complete_task(request, id):
    task = TaskStoreModel.objects.get(pk=id)
    task.completed = True
    task.save()
    return redirect('completed_task')
