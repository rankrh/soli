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


def createSelectInput(attrs):
    attributes = {
        'class': 'custom-select',
    }

    attributes = updateAttributes(attributes, attrs)

    return forms.Select(attrs=attributes)


def createRadioInput(placeholder):
    style = "custom-radio"

    attributes = {
        'class': style,
        'placeholder': placeholder
    }

    return forms.RadioSelect(attrs=attributes)


def updateAttributes(attributes, attrs):
    for attribute, value in attrs.items():
        if attribute in attributes:
            attributes[attribute] += " " + value
        else:
            attributes[attribute] = value

    return attributes
