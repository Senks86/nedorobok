from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

GROUPS = ["User", "Moderator", "Admin"]

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    # створюємо групи, якщо їх ще немає
    for name in GROUPS:
        Group.objects.get_or_create(name=name)
