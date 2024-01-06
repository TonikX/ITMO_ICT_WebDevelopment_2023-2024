# Формы

Дополнительно к моделям данных заведем две простые формы:

### 1. Форма регистрации

Админ добавляет юзера на рейс. Эта инфомрация отображается в его личном кабинете. Там же он может удалить бронь, или
изменить номер кресла (из оставшихся) и статус подтверждения регистрации.

```python
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['registered', 'seat']
```

### 2. Форма для создания отзыва

```python
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
```