from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from myapp.models import Item
from myapp.forms import ItemForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

@login_required
def item(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    # return HttpResponse(item_list)
    return render(request, "myapp/index.html", context=context)

def detail(request, id):
    item_detail = Item.objects.get(id=id)
    context = {
        "item_detail": item_detail
    }
    return render(request, "myapp/detail.html", context=context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:home')

    context = {
        'form': form
    }
    return render(request, "myapp/item-form.html", context)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:home')

    context = {
        'form': form
    }

    return render(request, "myapp/item-form.html", context)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("myapp:home")

    context = {
        'item': item
    }
    return render(request, "myapp/item-delete.html", context=context)
