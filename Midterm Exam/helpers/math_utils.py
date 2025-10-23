def area(length, width):
    return length * width

def area_improved(length: float, width: float) -> float:
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        return "Length and width must be numbers"
    return length * width