from django.contrib.auth import get_user_model
from django.apps import AppConfig
from django.db import models


class ReusableAppConfig(AppConfig):
    name = "reusable_app"
    verbose_name = "Reusable App"

    def ready(self):

        from .models import handle_user_save_signal, handle_user_delete_signal

        models.signals.post_save.connect(
            handle_user_save_signal,
            sender=get_user_model(),
            dispatch_uid='register_user_save'
        )
        models.signals.pre_delete.connect(
            handle_user_delete_signal,
            sender=get_user_model(),
            dispatch_uid='register_user_delete'
        )

