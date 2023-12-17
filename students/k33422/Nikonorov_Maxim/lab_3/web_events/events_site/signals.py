from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import SubscribedEmail, EventsUser, UsersEventsList

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