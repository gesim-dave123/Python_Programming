def shout(s) :
    return s.upper()

def shout_improved(s: str) -> str:
    """Return the string in uppercase."""
    if not isinstance(s, str):
        return "Input must be a string"
    return s.upper()