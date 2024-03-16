# ЛАБОРАТОРНАЯ РАБОТА №3 :  Реализация серверной части на django rest. Документирование API. #
**Цель:** Овладеть практическими навыками и умениями реализации web-сервисов средствами Django.

**Задание:** Реализовать сайт, используя фреймворк Django 3, Django REST Framework, Djoser и СУБД PostgreSQL, в соответствии с вариантом задания лабораторной работы.

## Выполнение работы ##
### Вариант 13 (из курса основы баз данных) ###
Создать программную систему, предназначенную для хранения информации о торгах на товарно-сырьевой бирже.

На торги могут быть представлены разные товары одной и той же фирмы и одни и те же товары разных фирм. Каждый товар имеет свой уникальный код, произведен определенной формой в определенное время. Товар имеет гарантийный срок хранения, единицу измерения. Товар считается просроченным, если дата его отгрузки более поздняя, чем дата производства этого товара в сумме с гарантийным сроком хранения. Товары поставляются партиями. Партия характеризуется: номером, количеством единиц в партии, ценой поставляемого товара, условиями поставки (предоплата или нет). Партии товаров выставляют брокеры.

В одну партию товаров включаются разнообразные товары от разных производителей. Считается, что партии товаров, выставленные на продажу, покупает сама биржа, и она же расплачивается с брокером и производителями товара. Если условием поставки указана предоплата, то биржа перечисляет деньги в день заключения договора, а если нет — то в день отгрузки.

Брокеры работают за фиксированный процент прибыли — 10% от суммы заключенных сделок. Ежемесячно брокеры перечисляют конторе, в которой они работают, фиксированную сумму денег, а все остальные заработанные ими деньги составляют их чистый доход (зарплату).

Перечень возможных запросов к базе данных:

* подсчитать, сколько единиц товара каждого вида выставлено на продажу от начала торгов до заданной даты;
* найти фирму-производителя товаров, которая за заданный период времени выручила максимальную сумму денег;
* найти товары, которые никогда не выставляли на продажу брокеры заданной конторы;
* найти все факты выставления на продажу товаров с просроченной годностью (номер партии, код товара, наименование товара, данные о брокере);
* найти зарплату всех брокеров заданной конторы.
Необходимо предусмотреть возможность получения отчета по последним торгам по всем товарам с указанием фирм, предлагающих товар в партиях, количества единиц, суммарного количества по торгам, общего количества наименований, участвующих в торгах.

![](l3_db.png)

**serializers.py**

```python
import datetime
from rest_framework import serializers
from .models import Consignment, Company, BrokerCompany, Broker, ProductByCompany, Product


class ProductSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CountProductSerialiser(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["count"]

    def get_count(self, obj):
        return ProductByCompany.objects.filter(product=obj.id, created__lt=self.context["date"]).count()


class DateSerializer(serializers.Serializer):
    date = serializers.DateField(default=datetime.date.today())

    class Meta:
        fields = ['date']


class ProductByCompanySerialiser(serializers.ModelSerializer):
    class Meta:
        model = ProductByCompany
        fields = "__all__"


class CompanySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class BrokerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = "__all__"


class CountBrokerSalarySerializer(serializers.ModelSerializer):

    salary = serializers.SerializerMethodField()

    class Meta:
        model = Broker
        fields = ['id', 'name', 'salary']

    def get_salary(self, obj):
        count = 0
        for c in Consignment.objects.filter(broker=obj.id):
            count = ProductByCompany.objects.filter(consignment=c.id).count() * c.cost
        return count


class BrokerCompanySerialiser(serializers.ModelSerializer):
    class Meta:
        model = BrokerCompany
        fields = "__all__"


class ConsignmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Consignment
        fields = "__all__"

class BrokerTopProductsSerializer(serializers.ModelSerializer):
    top_products = serializers.SerializerMethodField()

    class Meta:
        model = Broker
        fields = ['id', 'name', 'top_products']

    def get_top_products(self, obj):
        current_year = self.context['date'].year
        consignments = Consignment.objects.filter(broker=obj.id, date_sold__year=current_year)

        product_counts = {}

        for consignment in consignments:
            products_in_consignment = ProductByCompany.objects.filter(consignment=consignment.id)
            
            for product_by_company in products_in_consignment:
                product = product_by_company.product
                product_count = product_counts.get(product.id, 0)
                product_counts[product.id] = product_count + 1

        sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        top_products_data = []

        for product_id, count in sorted_products:
            product = Product.objects.get(id=product_id)
            top_products_data.append({
                'product_id': product_id,
                'product_name': product.name,
                'count': count,
            })

        return top_products_data
```

