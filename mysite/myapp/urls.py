from django.urls import path
from . import views

# assigning a namespace to prevent name conflict in url names when multiple apps are involved in our project
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'), # naming url - to replace hardcoded urls from being used within our project
    path('item/', views.item),
    path('<int:id>/', views.detail, name='detail'),
    path('add/', views.create_item, name="create-item"),
]
