from django.core.exceptions import ValidationError


def validate_sexo(value):
    valid_sexo = ['M', 'F', 'O']
    if value not in valid_sexo:
        raise ValidationError('Selecione um genero.')

