from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'form.html', {'form': form})

def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'form.html', {'form': form})

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'item': item})

def view_item(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'view.html', {'item': item})
