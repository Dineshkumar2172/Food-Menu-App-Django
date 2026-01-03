from django.urls import path
from users import views

# assigning a namespace to prevent name conflict in url names when multiple apps are involved in our project
app_name = 'users'

urlpatterns = [
    path('register/', views.register_user, name="register"),
]
