# Эндпоинты

Для каждой из моделей будем использовать `ModelViewSet` для реализации базовых REST запросов

=== "NewspaperViewSet"

    ```Python title="NewspaperViewSet"
    --8<-- "laboratory_work_3/newspapers/views.py:11:14"
    ```

=== "PrintingOfficeViewSet"

    ```Python title="PrintingOfficeViewSet"
    --8<-- "laboratory_work_3/newspapers/views.py:17:20"
    ```

=== "PostOfficeViewSet"

    ```Python title="PostOfficeViewSet"
    --8<-- "laboratory_work_3/newspapers/views.py:23:26"
    ```

=== "NewspaperEditionViewSet"

    ```Python title="NewspaperEditionViewSet"
    --8<-- "laboratory_work_3/newspapers/views.py:29:32"
    ```

=== "NewspaperOrderViewSet"

    ```Python title="NewspaperOrderViewSet"
    --8<-- "laboratory_work_3/newspapers/views.py:35:38"
    ```

=== "NewspaperDistributionViewSet"

    ```Python title="NewspaperDistributionViewSet"
    --8<-- "laboratory_work_3/newspapers/views.py:41:44"
    ```

Для более специфичных задач будем использовать декоратор `@api_view`

=== "printingAddressesByName"
    По каким адресам печатаются газеты данного наименования?

    ```Python title="printingAddressesByName"
    --8<-- "laboratory_work_3/newspapers/views.py:47:53"
    ```

=== "mostPrintedAuthor"
    Фамилия редактора газеты, которая печатается в указанной типографии самым
    большим тиражом?

    ```Python title="mostPrintedAuthor"
    --8<-- "laboratory_work_3/newspapers/views.py:56:72"
    ```

=== "distributionAddressesByPrice"
    На какие почтовые отделения (адреса) поступает газета, имеющая цену, больше
    указанной?

    ```Python title="distributionAddressesByPrice"
    --8<-- "laboratory_work_3/newspapers/views.py:75:85"
    ```

=== "lessCountDistributionAddresses"
    Какие газеты и куда (номер почты) поступают в количестве меньшем, чем
    заданное?

    ```Python title="lessCountDistributionAddresses"
    --8<-- "laboratory_work_3/newspapers/views.py:88:121"
    ```

=== "newspaperDistributionAddresses"
    Куда поступает данная газета, печатающаяся по данному адресу.

    ```Python title="newspaperDistributionAddresses"
    --8<-- "laboratory_work_3/newspapers/views.py:124:137"
    ```
