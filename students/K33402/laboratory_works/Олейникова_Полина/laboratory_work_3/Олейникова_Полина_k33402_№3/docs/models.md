# Модели


## Модель профиля
```
class Profile(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    location = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'location']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
```    

## Модель книги
```
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.title
```

## Модель запроса на обмен книгами
```
class ExchangeRequest(models.Model):
    statuses = (
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('notconsidered', 'Not considered'),
    )

    to_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book_offered = models.ForeignKey(Book, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    status = models.CharField(max_length=13, choices=statuses, default='notconsidered')
    
    def __str__(self):
        return f"user:{self.to_user} book:{self.book_offered}, {self.from_date} {self.to_date} {self.status}"
```