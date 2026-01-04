from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from myapp.models import Item
from myapp.forms import ItemForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

# @login_required
# def item(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list
#     }
#     # return HttpResponse(item_list)
#     return render(request, "myapp/index.html", context=context)

# implementing above item view using class based list view
class ItemClassView(ListView):
    model = Item
    template_name = "myapp/index.html"
    context_object_name = "item_list"

# def detail(request, id):
#     item_detail = Item.objects.get(id=id)
#     context = {
#         "item_detail": item_detail
#     }
#     return render(request, "myapp/detail.html", context=context)

# implementing above detail view using class based detail view
class DetailClassView(DetailView):
    # here it take pk as an parameter instead of id
    # it automatically handled getting detail based on pk (primary key)
    model = Item
    template_name = "myapp/detail.html"
    context_object_name = "item_detail"

# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:home')

#     context = {
#         'form': form
#     }
#     return render(request, "myapp/item-form.html", context)

class CreateClassView(CreateView):
    # whenever we create a class based createview, it always look for
    # the template with name <model_name>_form.html, for example if our model
    # is named as food, then it'll look for food_form.html from templates.
    # in our case it'll look for item_form.html.
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    context_object_name = "form"

# def update_item(request, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:home')

#     context = {
#         'form': form
#     }

#     return render(request, "myapp/item-form.html", context)

class UpdateClassView(UpdateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    template_name_suffix = "_update_form" # to configure template suffix to look for

# def delete_item(request, id):
#     item = Item.objects.get(id=id)
#     if request.method == "POST":
#         item.delete()
#         return redirect("myapp:home")

#     context = {
#         'item': item
#     }

#     return render(request, "myapp/item-delete.html", context=context)

class DeleteClassView(DeleteView):
    model = Item
    template_name_suffix = "-delete"
    context_object_name = "item"
    success_url = reverse_lazy("myapp:home")
