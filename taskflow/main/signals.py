from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import Project, Task
import logging

from django.db.models.signals import m2m_changed

logger = logging.getLogger('signals')


#project deleted/created
@receiver(post_delete, sender=Project)
def project_deleted(sender, instance, **kwargs):
    msg = f'DELETED Project: {instance.name}'
    logger.info(msg)
    print(f'[SIGNAL] {msg}')


@receiver(post_save, sender= Project)
def project_save(sender, instance, created, **kwargs):
    if created:
        msg = f'CREATED Project: {instance.name}'
    else: msg = f'UPDATE Project: {instance.name}'
    logger.info(msg)
    print(f'[SIGNAL] {msg}')


#TasK deleted/created
@receiver(post_delete, sender=Task)
def task_deleted(sender, instance, **kwargs):
    msg = f'DELETED Task: {instance.title}'
    logger.info(msg)
    print(f'[SIGNAL] {msg}')


@receiver(post_save, sender= Task)
def task_save(sender, instance, created, **kwargs):
    if created:
        msg = f'CREATED Task: {instance.title}'
    else: msg = f'UPDATE Task: {instance.title}'
    logger.info(msg)
    print(f'[SIGNAL] {msg}')





# LOGIN/LOGOUT
@receiver(user_logged_in)
def loggin_user(sender, request, user, **kwargs):
    msg = f'USER |{user}| => LOGGINED'
    logger.info(msg)
    print(f"[SIGNAL] {msg}")

@receiver(user_logged_out)
def loggin_out_user(sender, request, user, **kwargs):
    msg = f'USER |{user}| => LOGOUTED'
    logger.info(msg)
    print(f"[SIGNAL] {msg}")
