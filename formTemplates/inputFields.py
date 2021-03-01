from datetime import date

from django import forms


def createNumberInput(placeholder=None, minimum=None, maximum=None):
    attributes = {
        'class': 'form-control number',
        'placeholder': placeholder,
        'min': minimum,
        'max': maximum
    }

    return forms.NumberInput(attrs=attributes)


def createTextInput(placeholder, id=None):
    attributes = {
        'class': 'form-control',
        'placeholder': placeholder,
    }

    if id:
        attributes["id"] = id

    return forms.TextInput(attrs=attributes)


def createTextArea(placeholder="", rows=5):
    attributes = {
        "class": "form-control",
        "rows": rows,
        "placeholder": placeholder
    }

    return forms.Textarea(attributes)


def createSelectInput(placeholder="", extraClasses=[], attrs={}):
    classes = "custom-select"
    for extraClass in extraClasses:
        classes += " " + str(extraClass)

    attributes = {
        **{
            'class': classes,
            'placeholder': placeholder,
        },
        **attrs}

    return forms.Select(attrs=attributes)


def createRadioInput(placeholder=None, choices=[], onchange=None):
    choices = [(choice[0], choice[1].capitalize()) for choice in choices]
    attributes = {
        'placeholder': placeholder
    }
    if onchange:
        attributes["onchange"] = onchange

    return forms.RadioSelect(attrs=attributes, choices=choices)


def createImageUpload(id=None):
    attrs = {}
    if id is not None:
        attrs["id"] = id

    return forms.ClearableFileInput(attrs=attrs)


def updateAttributes(attributes, attrs):
    for attribute, value in attrs.items():
        if attribute in attributes:
            attributes[attribute] += " " + value
        else:
            attributes[attribute] = value

    return attributes


def createYearInput(yearMin=None, yearMax=None):
    yearMin = 1900 if yearMin is None else yearMin
    yearMax = date.today().year if yearMax is None else yearMax

    return createNumberInput(minimum=yearMin, maximum=yearMax)


def createDateInput(placeholder=None):
    attributes = {
        "class": "form-control",
        "placeholder": placeholder if placeholder is not None else ""
    }

    return forms.DateInput(attrs=attributes)
