### views.py (представления)

#### basket/views.py
```python
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
```
#### main/views.py
```python
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product, Category
from django.db.models import Q
from .forms import SignUpForm
def frontpage(request):
    products = Product.objects.all()

    return render(request, 'main/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'main/signup.html', {'form': form})

@login_required
def mypage(request):
    return render(request, 'main/mypage.html')

@login_required
def mypage_edit(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('mypage')
    return render(request, 'main/mypage_edit.html')

def store(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }
    return render(request, 'main/store.html', context)
```
### order/views.py
```python
from django.shortcuts import render, redirect

from basket.basket import Basket

from .models import Order, OrderItem

def start_order(request):
    basket = Basket(request)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')

        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, zipcode=zipcode, place=place)

        for item in basket:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        return redirect('mypage')
    return redirect('basket')
```
#### main/views.py
```python
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect('product', slug=slug)

    return render(request, 'products/product.html', {'product': product})
```
