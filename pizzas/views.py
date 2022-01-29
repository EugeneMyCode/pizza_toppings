from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

# Create your views here.

def index(request):
    """"Домашняя страница приложения Pizzeria"""
    return render(request, 'pizzas/index.html')

@login_required
def pizzas(request):
    """"Выводит список пицц"""
    pizzas = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

@login_required
def pizza(request, pizza_id):
    """"Выводит одну пиццу и все её топпинги"""
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.owner != request.user:
        raise Http404

    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)

@login_required
def new_pizza(request):
    """"Определяет новый топпинг"""
    if request.method != 'POST':
        form = PizzaForm()
    else:
        """"Обрабатываем данные POST"""
        form = PizzaForm(request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()
            return redirect('pizzas:pizzas')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'pizzas/new_pizza.html', context)

@login_required
def new_topping(request, pizza_id):
    """"Добавляет новый топпинг"""
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ToppingForm()
    else:
        """"Обрабатываем данные POST"""
        form = ToppingForm(request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    # Вывести пустую или недействительную форму
    context = {'pizza': pizza, 'form': form}
    return render(request, 'pizzas/new_topping.html', context)

@login_required
def edit_topping(request, topping_id):
    """"Редактирует топпинг"""
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza
    if pizza.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(request.POST, instance=topping)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza.id)

    context = {'topping': topping, 'pizza': pizza, 'form': form}
    return render(request, 'pizzas/edit_topping.html', context)