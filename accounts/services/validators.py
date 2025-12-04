from django.core.exceptions import ValidationError

def validate_username(username):
    """
    Basic validation for username.
    """
    if username is None:
        raise ValidationError("Username is required.")

    username = username.strip()
    if not username:
        raise ValidationError("Username is required.")

    if len(username) > 10:
        raise ValidationError("Username must be at most 10 characters long.")

    return username


def validate_full_name(full_name):
    """
    Basic validation for full name.
    """
    if full_name is None:
        raise ValidationError("Full name is required.")

    full_name = full_name.strip()
    if not full_name:
        raise ValidationError("Full name is required.")

    if len(full_name) > 50:
        raise ValidationError("Full name must be at most 50 characters long.")

    return full_name

def validate_age(age):
    """
    Basic validation for age.
    """
    if age is None:
        raise ValidationError("Age is required.")

    if age < 14:
        raise ValidationError("You must be at least 14 years old to sign up.")

    if age > 100:
        raise ValidationError("Please enter a realistic age (100 or below).")

    return age

def validate_phone_number(phone_number):
    """
    Basic validation for phone number.
    """
    if phone_number is None:
        raise ValidationError("Phone number is required.")

    phone_number = phone_number.strip()

    if not phone_number:
        raise ValidationError("Phone number is required.")

    if not phone_number.isdigit():
        raise ValidationError("Phone number should contain digits only.")

    if not (9 <= len(phone_number) <= 15):
        raise ValidationError("Phone number should be between 9 and 15 digits.")

    return phone_number

def validate_email_address(email):
    """
    Very simple email validation for teaching purposes.
    This is deliberately simple and not a full email validator.
    """
    if email is None:
        raise ValidationError("Email address is required.")

    email = email.strip()
    if not email:
        raise ValidationError("Email address is required.")

    if "@" not in email:
        raise ValidationError("Email address must contain '@'.")

    at_index = email.index("@") # safe because we just checked it's present

    if at_index == 0 or at_index == len(email) - 1:
        raise ValidationError("Email address cannot start or end with '@'.")

    return email

def validate_password(password):
    """
    Basic validation for password.
    """
    if password is None:
        raise ValidationError("Password is required.")

    password = password.strip()
    if not password:
        raise ValidationError("Password is required.")

    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    if not any(ch.isdigit() for ch in password):
        raise ValidationError("Password should contain at least one digit.")

    return password

def validate_confirm_password(password, confirm_password):
    """
    Check that confirm_password matches password.
    """
    if confirm_password is None:
        raise ValidationError("Please confirm your password.")

    confirm_password = confirm_password.strip()
    if not confirm_password:
        raise ValidationError("Please confirm your password.")

    if password != confirm_password:
        raise ValidationError("Passwords do not match.")

    return confirm_password

def validate_agree_to_terms(agree_to_terms):
    """
    Basic validation for 'agree to terms' checkbox.
    """
    if agree_to_terms is not True:
        raise ValidationError("You must agree to the terms to sign up.")

    return agree_to_terms
