from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .basket import Basket
from products.models import Product

def add_basket(request, product_id):
    basket = Basket(request)
    basket.add(product_id)

    return render(request, 'basket/basket_menu.html')

def basket(request):
    return render(request, 'basket/basket.html')


def update_basket(request, product_id, action):
    basket = Basket(request)
    quantity = 1
    if action == 'increment':
        basket.add(product_id, 1, True)
    else:
        basket.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    item = basket.get_item(product_id)
    if item is not None:
        quantity = item['quantity']


    item = {
        'product': {
            'id': product.id,
            'name': product.name,
            'image': product.image,
            'price': product.price,
        },

        'quantity': quantity,
        'total_price': (quantity * product.price) / 100,
    }

    response = render(request, 'basket/partials/basket_item.html', {'item': item})
    response['HX-Trigger'] = 'update-basket-menu'

    return response

@login_required()
def checkout(request):
    return render(request, 'basket/checkout.html')

def hx_basket_menu(request):
    return render(request, 'basket/basket_menu.html')

def hx_basket_total(request):
    return render(request, 'basket/partials/basket_total.html')