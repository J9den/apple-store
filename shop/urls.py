from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    # Заглушка под корзину (пока без логики) — ВЫШЕ detail по slug
    path('cart/add/<int:product_id>/', views.cart_add_stub, name='cart_add'),

    # detail по slug — ПОСЛЕДНИМ
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
