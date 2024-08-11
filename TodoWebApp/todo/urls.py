from django.urls import path

from todo.views import index, remove
urlpatterns = [
    path('home/', index, name='todohome'),
    path('del/<str:item_id>', remove, name='delete'),
]
