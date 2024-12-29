from django.urls import path
from rest_framework import routers

from .views.access_recovery_views import restore_password_step1, restore_password_step2
from .views.authentication_views import get_new_token_pair
from .views.logout_views import logout, logout_all
from .views.registration_views import register_step_1, register_step_2
from .views.user_views import (UserViewSet, UserPasswordChange, UserAvatarChange, UserPrivateDataChange,
                               UserEmailChange)
from .views.authorize_views import authorize

router = routers.DefaultRouter()
router.register("users", UserViewSet)
urlpatterns = [
    path("users/register/step1", register_step_1),
    path("users/register/step2", register_step_2),
    path("users/change/password", UserPasswordChange.as_view()),
    path("users/change/avatar", UserAvatarChange.as_view()),
    path("users/change/private_data", UserPrivateDataChange.as_view()),
    path("users/change/email", UserEmailChange.as_view()),
    path("auth/login", authorize),
    path("auth/logout", logout),
    path("auth/full-logout", logout_all),
    path("auth/token-pair", get_new_token_pair),
    path("auth/recover-password", restore_password_step1),
    path("auth/confirm-password", restore_password_step2)
] + router.urls
