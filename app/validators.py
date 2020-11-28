from django import forms


def ingredients_validator(value):
    if ',' not in value:
        raise forms.ValidationError('The ingredients must be separated by ","')
