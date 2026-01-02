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
