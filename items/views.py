from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Read: List all item
def item_list(request):
    items = Item.objects.all().order_by('-created_at') # yangi qo'shilgan ma'lumotlar tepadan chiqadi
    return render(request, 'item_list.html', {'items': items})

# Create: Add a new item
def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
        return render(request, 'item_form.html', {'form': form})


# Update: Edit an existing item
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

# Delete: Rmove an item
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})