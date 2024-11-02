from django.shortcuts import redirect, render

# import todo form and models

from .models import Todo
from .forms import TodoForm

###############################################


def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    return redirect('todo')