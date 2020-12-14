UNKNOWN = "unknown"


ORGANIC = "organic"
NOT_ORGANIC = "commercial"

ORGANIC_CHOICES = [
    (True, ORGANIC),
    (False, NOT_ORGANIC),
    (None, UNKNOWN)
]

TREATED = "treated"
UNTREATED = "untreated"

TREATED_CHOICES = [
    (True, TREATED),
    (False, UNTREATED),
    (None, UNKNOWN)
]

HYBRID = "hybrid"
OPEN_POLLINATED = "open pollinated"

HYBRID_CHOICES = [
    (True, HYBRID),
    (False, OPEN_POLLINATED),
    (None, UNKNOWN)
]