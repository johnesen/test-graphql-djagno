import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    full_name = models.CharField(
        blank=True, null=True, max_length=100, verbose_name=_("fullname")
    )
    email = models.EmailField(_("email"), unique=True, null=True, blank=True)
    password = models.CharField(
        max_length=128, blank=True, null=True, verbose_name=_("password")
    )
    photo = models.ImageField(
        _("profile photo"), upload_to="user_media/%Y/%m/%d/", null=True, blank=True
    )
    is_active = models.BooleanField(default=False, verbose_name=_("активирован"))
    is_superuser = models.BooleanField(
        default=False, verbose_name=_("админ пользовател")
    )
    is_deleted = models.BooleanField(default=False, verbose_name=_("удалить"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("дата создания")
    )
