from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import phone_validator
from .managers import CustomUserManager





class User(AbstractUser):
    username = None
    phone_no = models.CharField(
        max_length=15,
        unique=True,
        validators=[phone_validator],
        error_messages={
            'unique': _("A user with that phone number already exists."),
        },
    )
    email = models.EmailField(_('email'), unique=True, blank=True, null=True)

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_no
