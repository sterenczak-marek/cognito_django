from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User

    def get_object(self, queryset=None):
        return self.request.user
