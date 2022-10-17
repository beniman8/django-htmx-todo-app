
from django.urls import path
from .views import todo,add_todo,update_todo,delete_todo
urlpatterns = [
    path('', todo, name='home'),
    path('add-todo/', add_todo, name='add-todo'),
    path('update-todo/<int:pk>/', update_todo, name='update-todo'),
    path('delete/<int:pk>/', delete_todo, name='delete-todo'),
]
