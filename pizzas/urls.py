""""Схемы URL для Pizzas"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех пицц
    path('pizzas/', views.pizzas, name='pizzas'),
    # Страница с топпингами
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    # Страница для добавления новой пиццы
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    # Страница для редактирования топпинга
    path('edit_topping/<int:topping_id>/', views.edit_topping, name='edit_topping'),
    # Страница для добалвнеия топпинга к пицце
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping')
    ]