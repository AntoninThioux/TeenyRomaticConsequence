"""My Module."""
import jwt


def romance(x: int, y: int):
    """Romance."""
    print(f"{x} x {y} = {x*y}")
    return x*y


def more_romance(payload: dict) -> str:
    """More."""
    return jwt.encode(payload, "teeny")
