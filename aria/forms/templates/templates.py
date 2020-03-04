from django import forms


def createNumberInput(placeholder, minimum=None, maximum=None):
    attributes = {
        'class': 'mx-3 mb-3 form-control number',
        'placeholder': placeholder,
    }

    if minimum is not None:
        attributes["min"] = minimum

    if maximum is not None:
        attributes["max"] = maximum

    return forms.NumberInput(attrs=attributes)


def createTextInput(placeholder):
    attributes = {
        'class': 'mx-3 mb-3 form-control',
        'placeholder': placeholder
    }

    return forms.TextInput(attrs=attributes)


def createSelectInput(attrs):
    attributes = {
        'class': 'mx-3 mb-3 custom-select',
    }

    attributes = updateAttributes(attributes, attrs)

    return forms.Select(attrs=attributes)


def createRadioInput(placeholder):
    style = "mx-3 custom-radio ml-4"

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
