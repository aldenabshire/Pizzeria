from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):

	"""The home page for Learning Log."""
	return render(request, 'pizzas/index.html')

def pizzas(request):

    pizzas = Pizza.objects.order_by('pizza_name')

    context = {'p':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):

    p = Pizza.objects.get(id = pizza_id)
    toppings = Toppings.objects.filter(pizza = p)
    comments = Comment.objects.filter(pizza = p)

    context = {'pizza':p, 'toppings':toppings, 'comments':comments}

    return render(request, 'pizzas/pizza.html', context)

def new_comment(request, pizza_id):

    pizza = Pizza.objects.get(id = pizza_id)

    if request.method != 'POST':

        form = CommentForm()

    else:

        print(request.POST)
        form = CommentForm(data = request.POST)

        if form.is_valid():

            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza', pizza_id = pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html', context)