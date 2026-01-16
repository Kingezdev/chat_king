import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class SpecialCharacterValidator:
    """Validate that the password contains at least one special character."""
    def validate(self, password, user=None):
        if not re.findall('[^\w\s]', password):
            raise ValidationError(
                _("The password must contain at least one special character."),
                code='password_no_special',
            )

    def get_help_text(self):
        return _("Your password must contain at least one special character.")

class UppercaseValidator:
    """Validate that the password contains at least one uppercase letter."""
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least one uppercase letter."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _("Your password must contain at least one uppercase letter.")

class LowercaseValidator:
    """Validate that the password contains at least one lowercase letter."""
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least one lowercase letter."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _("Your password must contain at least one lowercase letter.")

class NumberValidator:
    """Validate that the password contains at least one number."""
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least one number."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _("Your password must contain at least one number.")

def validate_password_strength(value):
    """Validate that a password meets minimum strength requirements."""
    min_length = 8
    
    if len(value) < min_length:
        raise ValidationError(
            _('Password must be at least %(min_length)d characters long.'),
            code='password_too_short',
            params={'min_length': min_length},
        )
        
    # Check for common patterns
    common_patterns = [
        '123456', 'password', 'qwerty', '111111', 'abc123'
    ]
    
    if any(pattern in value.lower() for pattern in common_patterns):
        raise ValidationError(
            _('This password is too common or easily guessable.'),
            code='password_too_common',
        )
