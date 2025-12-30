from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    """Display all todos"""
    todos = Todo.objects.all()
    
    # Filter by status if requested
    filter_status = request.GET.get('filter', 'all')
    if filter_status == 'active':
        todos = todos.filter(is_resolved=False)
    elif filter_status == 'completed':
        todos = todos.filter(is_resolved=True)
    elif filter_status == 'overdue':
        todos = [todo for todo in todos if todo.is_overdue()]
    
    context = {
        'todos': todos,
        'filter_status': filter_status,
    }
    return render(request, 'todos/todo_list.html', context)


def todo_create(request):
    """Create a new todo"""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo created successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    return render(request, 'todos/todo_form.html', {'form': form, 'action': 'Create'})


def todo_edit(request, pk):
    """Edit an existing todo"""
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'todos/todo_form.html', {'form': form, 'todo': todo, 'action': 'Edit'})


def todo_delete(request, pk):
    """Delete a todo"""
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo deleted successfully!')
        return redirect('todo_list')
    
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})


def todo_toggle_resolved(request, pk):
    """Toggle the resolved status of a todo"""
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_resolved = not todo.is_resolved
    todo.save()
    
    status = 'completed' if todo.is_resolved else 'reopened'
    messages.success(request, f'Todo {status} successfully!')
    
    return redirect('todo_list')

