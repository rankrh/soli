from django import forms


def createNumberInput(placeholder=None, minimum=None, maximum=None):
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


def createTextArea(placeholder, rows=5):
    attributes = {
        "class": "form-control",
        "rows": rows,
        "placeholder": placeholder
    }

    return forms.Textarea(attributes)


def createSelectInput(placeholder="", extraClasses=[]):

    classes = "custom-select"
    for extraClass in extraClasses:
        classes += " " + str(extraClass)

    attributes = {
        'class': classes,
        'placeholder': placeholder,
    }

    return forms.Select(attrs=attributes)


def createRadioInput(placeholder=None, choices=[]):

    choices = [(choice[0], choice[1].capitalize()) for choice in choices]
    attributes = {
        'placeholder': placeholder
    }

    return forms.RadioSelect(attrs=attributes, choices=choices)


def updateAttributes(attributes, attrs):
    for attribute, value in attrs.items():
        if attribute in attributes:
            attributes[attribute] += " " + value
        else:
            attributes[attribute] = value

    return attributes
