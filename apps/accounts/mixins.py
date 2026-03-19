from django.contrib.auth.mixins import UserPassesTestMixin

class ModeratorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return u.is_authenticated and (
            u.is_superuser or u.groups.filter(name__in=["Moderator", "Admin"]).exists()
        )

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return u.is_authenticated and (u.is_superuser or u.groups.filter(name="Admin").exists())
