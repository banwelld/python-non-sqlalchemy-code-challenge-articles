def enforce_type(value, expected: type):
    if not isinstance(value, expected):
        raise ValueError(err_msg_type(expected.__name__, type(value)))
    
def enforce_min_len(value, min_length: int):
    if len(value) < min_length:
        raise ValueError(err_msg_len(value, min_length))
    
def enforce_max_len(value, max_length: int):
    if len(value) >= max_length:
        raise ValueError(err_msg_len(value, max_length))   
    
def err_msg_type(expected, actual) -> str:
    return (
        f"Attribute value is of wrong type (expected: '{expected}'; "
        f"got: '{actual}')"
    )

def err_msg_len(value: str, limit: int) -> str:
    rule = "maximum" if len(value) > limit else "minimum"
    return (
        f"'{value}' invalid: length outside expected range ({rule}: {limit} "
        f"characters; actual: {len(value)} characters)."
    )