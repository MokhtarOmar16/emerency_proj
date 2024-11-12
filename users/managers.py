from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    
    def create_user(self, phone_no, password=None, **extra_fields):
        if not phone_no:
            raise ValueError('The Phone Number field is required')
        user = self.model(phone_no=phone_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, phone_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_no, password, **extra_fields)