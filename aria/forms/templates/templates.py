from django import forms


def createNumberInput(placeholder, minimum=None, maximum=None):
    attributes = {
        'class': 'mb-3 form-control number',
        'placeholder': placeholder,
    }

    if minimum is not None:
        attributes["min"] = minimum

    if maximum is not None:
        attributes["max"] = maximum

    return forms.NumberInput(attrs=attributes)


def createTextInput(placeholder):
    attributes = {
        'class': 'mb-3 form-control',
        'placeholder': placeholder
    }

    return forms.TextInput(attrs=attributes)


def createSelectInput(placeholder):
    attributes = {
        'class': 'mb-3 custom-select',
        'placeholder': placeholder
    }

    return forms.Select(attrs=attributes)


def createRadioInput(placeholder):

    style = "custom-radio ml-4"

    attributes = {
        'class': style,
        'placeholder': placeholder
    }

    return forms.RadioSelect(attrs=attributes)
