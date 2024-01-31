# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import ct_scan_nodule_1, Mandatory_questionaire_fg, History

User = get_user_model()

@receiver(post_save, sender=ct_scan_nodule_1)
@receiver(post_save, sender=Mandatory_questionaire_fg)
def track_changes(sender, instance, created, **kwargs):
    if not created:
        user = kwargs.get('user', None)
      
        if user is None and hasattr(instance, 'user'):
            user = instance.user

        if user is not None:
            history = History(
                user=user,
                content_type=ContentType.objects.get_for_model(instance),
                object_id=instance.id,
                field_name='__all__',  
                old_value='__previous_value__', 
                new_value=str(instance),
            )
            print('saved history')
            history.save()
    print('not saved history')
