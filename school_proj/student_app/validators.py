from django.core.exceptions import ValidationError
import re

def validate_name(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    regex = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$' 
    valid_name = re.match(regex, name)

    if valid_name:
        return name
    else:
        raise ValidationError(error_message, params={'name': name})


def validate_email(email):
    error_message =  'Invalid school email format. Please use an email ending with "@school.com".'
    regex = r'^[a-zA-Z]+@school\.com$'
    valid_email = re.match(regex, email)

    if valid_email:
        return email
    else:
        raise ValidationError(error_message, params={'email': email})
    
def validate_combination_format(locker_combination):
    error_message = 'Combination must be in the format "12-12-12"'
    regex = r'^\d{2}-\d{2}-\d{2}$'
    valid_locker_combination = re.match(regex, locker_combination)

    if valid_locker_combination:
        return locker_combination
    else:
        raise ValidationError(error_message, params={'locker_combination': locker_combination})