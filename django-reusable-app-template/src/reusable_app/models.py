from typing import TYPE_CHECKING
from django.db import models
from django.conf import settings

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser



class UserChange(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        related_name="changes",
        null=True
    )
    deleted_user_id = models.IntegerField(null=True)

    class ActionType(models.TextChoices):
        CREATED = 'created', 'Created'
        UPDATED = 'updated', 'Updated'
        DELETED = 'deleted', 'Deleted'

    action_type = models.CharField(choices=ActionType.choices, max_length=32)


def handle_user_save_signal(instance: 'AbstractUser', created: bool, **kwargs):
    return UserChange.objects.create(
        action_type=UserChange.ActionType.CREATED if created else UserChange.ActionType.UPDATED,
        user=instance
    )


def handle_user_delete_signal(instance: 'AbstractUser', **kwargs):
    UserChange.objects.filter(user=instance).update(
        user_id=None, deleted_user_id=instance.pk
    )
    return UserChange.objects.create(
        action_type=UserChange.ActionType.DELETED, deleted_user_id=instance.pk
    )