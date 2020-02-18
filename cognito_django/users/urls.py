from django.urls import path

from cognito_django.users.views import (
    UserDetailView,
)

app_name = "users"
urlpatterns = [
    path("me/", view=UserDetailView.as_view(), name="detail"),
]
