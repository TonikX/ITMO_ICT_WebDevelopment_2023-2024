from django.conf import settings
from products.models import Product


class Basket(object):
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)

        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}

        self.basket = basket

    def __iter__(self):
        for p in self.basket.keys():
            self.basket[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.basket.values():
            item['total_price'] = int(item['product'].price * item['quantity']) / 100

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:
            self.basket[product_id]['quantity'] += int(quantity)

            if self.basket[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_cost(self):
        for p in self.basket.keys():
            self.basket[str(p)]['product'] = Product.objects.get(pk=p)

        return int(sum(item['product'].price * item['quantity'] for item in self.basket.values())) / 100

    def get_item(self, product_id):
        if product_id in self.basket:
            return self.basket[str(product_id)]
        else:
            return None
