## Сигналы

Так как на моем сайте некоторые модели зависят от изменениях в других, то я написал сигналы, которые бы обрабатывали эти изменения. Для реализации поставленной задачи я создал отдельный файл `signals.py`.

### Обновление списка почт для рассылки

Список почт динамически обновляется после того, как пользователь нажимает соответствующую галочку в личном кабинете.

``` py title="signals.py"
@receiver(post_save, sender=EventsUser)
def add_subscribed_email(sender, instance, **kwargs):
    if instance.IsSubscribed:
        subscribed_email, created = SubscribedEmail.objects.get_or_create(User=instance)
        subscribed_email.Email = instance.email  
        subscribed_email.save()
        print('E-mail added')

@receiver(post_save, sender=EventsUser)
def remove_subscribed_email(sender, instance, **kwargs):
    if not instance.IsSubscribed:
        try:
            subscribed_email = SubscribedEmail.objects.get(User=instance)
            subscribed_email.delete()
            print('E-mail deleted')
        except SubscribedEmail.DoesNotExist:
            pass
        
```
### Закрытие регистрации на мероприятие

Если на мероприятие записалось предельное количество пользователей, то регистрация на него закрывается. При этом, если кто-то отпишется, то регистрация открывается заново.

``` py title="signals.py"
@receiver(post_save, sender=UsersEventsList)
@receiver(post_delete, sender=UsersEventsList)
def update_event_status(sender, instance, **kwargs):
    event_card = instance.EventCard
    if event_card.NumberOfParticipants <= event_card.events_users_list.count() and event_card.Status != 'CANCELED':
            event_card.Status = 'CLOSED'
            event_card.save()
            print('Registration is closed')
    elif event_card.NumberOfParticipants > event_card.events_users_list.count() and event_card.Status != 'CANCELED':
            event_card.Status = 'OPENED'
            event_card.save()
            print('Registration is opened')
```