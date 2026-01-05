from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from myapp.models import Item
from myapp.forms import ItemForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

# @login_required
def item(request):
    item_list = Item.objects.all()

    # implementing pagination
    paginator = Paginator(item_list, 5)
    page_number = request.GET.get("page") # get page number from client ?page=<page_number>
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
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

############################# Class Bases Views #############################

# # implementing above item view using class based list view
# class ItemClassView(ListView):
#     model = Item
#     template_name = "myapp/index.html"
#     context_object_name = "item_list"

# # implementing above detail view using class based detail view
# class DetailClassView(DetailView):
#     # here it take pk as an parameter instead of id
#     # it automatically handled getting detail based on pk (primary key)
#     model = Item
#     template_name = "myapp/detail.html"
#     context_object_name = "item_detail"

# class CreateClassView(CreateView):
#     # whenever we create a class based createview, it always look for
#     # the template with name <model_name>_form.html, for example if our model
#     # is named as food, then it'll look for food_form.html from templates.
#     # in our case it'll look for item_form.html.
#     model = Item
#     fields = ["item_name", "item_desc", "item_price", "item_image"]
#     # updates the form to include username while submitting new record to DB through ORM
#     def form_valid(self, form):
#         form.instance.user_name = self.request.user
#         return super().form_valid(form)

# class UpdateClassView(UpdateView):
#     model = Item
#     fields = ["item_name", "item_desc", "item_price", "item_image"]
#     template_name_suffix = "_update_form" # to configure template suffix to look for
    
#     # overridden queryset to fetch items only belonging to current user.
#     # as this method is overridden, internally it prevents accessing records belonging to other users
#     # hence preventing users from updating items belonging to different users
#     def get_queryset(self):
#         return Item.objects.filter(user_name=self.request.user)

# class DeleteClassView(DeleteView):
#     model = Item
#     template_name_suffix = "-delete"
#     context_object_name = "item"
#     success_url = reverse_lazy("myapp:home")
