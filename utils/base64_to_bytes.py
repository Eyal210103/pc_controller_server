import base64


def base64_to_bytes(base64stream: str) -> bytes:
    return base64.b64decode(base64stream)
