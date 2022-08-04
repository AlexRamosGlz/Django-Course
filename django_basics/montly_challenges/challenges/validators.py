from django.core.exceptions import ValidationError

def validateIsNotLessThan0(value):
    if value < 0:
        raise ValidationError((f'{value}s is less than 0 '), params={'value': value})


def validatePassword(value):

    if not(len(value > 8)):
        raise ValidationError((f'password at least have more than 8 characters'))


