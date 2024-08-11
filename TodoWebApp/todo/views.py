from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from todo.forms import TodoForm
from todo.models import Todo
from users.models import CustomUser


# Create your views here.

@login_required
def index(request):
    userid = request.user.id
    item_list = Todo.objects.filter(user_id=userid).order_by("priority")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            my_user = request.user
            my_user2 = CustomUser.objects.get(email=my_user)
            obj.user = my_user2
            form.save()
            return redirect('todohome')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/home.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todohome')