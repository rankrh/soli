from django import forms


def createNumberInput(placeholder, minimum=None, maximum=None):
    attributes = {
        'class': 'form-control number',
        'placeholder': placeholder,
    }

    if minimum is not None:
        attributes["min"] = minimum

    if maximum is not None:
        attributes["max"] = maximum

    return forms.NumberInput(attrs=attributes)


def createTextInput(placeholder):
    attributes = {
        'class': 'form-control',
        'placeholder': placeholder
    }

    return forms.TextInput(attrs=attributes)


def createSelectInput(placeholder):
    attributes = {
        'class': 'custom-select mb-2 mr-sm-2 mb-sm-0',
        'placeholder': placeholder
    }

    return forms.Select(attrs=attributes)


def createRadioInput(placeholder, inline=False):

    style = "custom-control custom-radio"

    if inline:
        style += " custom-control-inline"

    attributes = {
        'class': style,
        'placeholder': placeholder
    }

    return forms.RadioSelect(attrs=attributes)
