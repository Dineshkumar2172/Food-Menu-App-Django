from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Item

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

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

