# Модели

### Импорты

```
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

```

### Работа с юзером

```
class CustomUserManager(BaseUserManager):
    def create_user(self, username, type, password):

        user = self.model(
            username=username,
            type=type,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, type, password):
        user = self.model(
            username=username,
            type='A',
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):

    id = models.BigAutoField(primary_key=True)

    type = models.TextField(choices=(('A', 'A'), ('P', 'P'), ('PO', 'PO'), ('N', 'N')))
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    linkedin_token = models.TextField(blank=True, default='')

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['type']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
```


### Газета

```
class Newspaper(models.Model):
    name = models.CharField(max_length=500)
    index = models.CharField(max_length=100)
    redactor_last_name = models.CharField(max_length=100)
    redactor_first_name = models.CharField(max_length=100)
    redactor_patronic = models.CharField(max_length=100)
    cost = models.FloatField()
```


### Почта

```
class PostOffice(models.Model):
    num = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
```


### Типография

```
class Printer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    max_capacity = models.IntegerField()
```


### Печать газеты

```
class PrintingNewspaper(models.Model):
    newspaper = models.ForeignKey('system.Newspaper', related_name='where_to_print', on_delete=models.CASCADE)
    printer = models.ForeignKey('system.Printer', related_name='what_is_printed', on_delete=models.CASCADE)
    how_many_to_print = models.IntegerField()
```

### Заказ почты

```
class PostOfficeOrder(models.Model):
    newspaper = models.ForeignKey('system.Newspaper', related_name='needed_in', on_delete=models.CASCADE)
    post_office = models.ForeignKey('system.PostOffice', related_name='what_is_needed', on_delete=models.CASCADE)
    how_many_needed = models.IntegerField()
```

### Доставка

```
class Transportation(models.Model):
    printing_newspaper = models.ForeignKey('system.PrintingNewspaper', related_name='printed_for',
                                           on_delete=models.CASCADE)
    post_office_order = models.ForeignKey('system.PostOfficeOrder', related_name='printed_by',
                                          on_delete=models.CASCADE)

    amount = models.IntegerField()

```