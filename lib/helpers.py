def validate_attribute(
    value,
    expected: type,
    min_length: int = None,
    max_length: int = None
):
    if not isinstance(value, expected):
        raise ValueError(err_msg_type(expected.__name__, type(value)))
    if min_length and len(value) < min_length:
        raise ValueError(err_msg_len(value, min_length))
    if max_length and len(value) > max_length:
        raise ValueError(err_msg_len(value, max_length))

def err_msg_type(expected, actual) -> str:
    return (
        f"Attribute value is of wrong type (expected: '{expected}', "
        f"received: '{actual}')"
    )

def err_msg_len(value: str, limit: int) -> str:
    rule = "maximum" if len(value) > limit else "minimum"
    return (
        f"'{value}' not within allowed length parameters ({rule}: '{limit}', "
        f"actual: '{len(value)}')"
    )