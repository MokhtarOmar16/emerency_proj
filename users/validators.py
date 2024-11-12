from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    r'^\d{9,20}$',
    'Enter a valid phone number with 9 to 20 digits.'
)