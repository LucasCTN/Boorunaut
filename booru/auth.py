# Thanks to https://github.com/baseplate-admin/CoreProject/blob/abc9387793ebeab2cc86b64b2cb005f1173e5962/backend/django_core/apps/api/auth.py#L30-L43
# Github issue: https://github.com/vitalik/django-ninja/issues/784
from typing import Any, Type

import django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from ninja_extra.security import AsyncHttpBearer, HttpBearer

from ninja_jwt.authentication import JWTBaseAuthentication
from ninja_jwt.tokens import Token
from .account.models import Account
# from ninja.compatibility import get_headers
from django.conf import settings
import logging


logger = logging.getLogger("django")

class AuthBearer(HttpBearer):
    def authenticate(
        self,
        request: HttpRequest,
        token: str,
    ) -> Account | AnonymousUser:
        try:
            token_data = Token.objects.get(token=token)
            return token_data.user
        except Token.DoesNotExist:
            return AnonymousUser

# class OptionalAuthBearer(AuthBearer):
#     def __call__(self, request: HttpRequest) -> Any | None:
#         headers = get_headers(request)
#         auth_value = headers.get(self.header)
#         if not auth_value:
#             return AnonymousUser()  # if there is no key, we return AnonymousUser object
#         parts = auth_value.split(" ")

#         if parts[0].lower() != self.openapi_scheme:
#             if settings.DEBUG:
#                 logger.error(f"Unexpected auth - '{auth_value}'")
#             return None
#         token = " ".join(parts[1:])
#         return self.authenticate(request, token)

# class OptionalJWTAuth(JWTBaseAuthentication, OptionalAuthBearer):
class OptionalJWTAuth(JWTBaseAuthentication, AuthBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Any:
        return self.jwt_authenticate(request, token)
