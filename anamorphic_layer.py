import os
import base64

def embed_secret_into_cover(cover_ciphertext: bytes, secret_message: str) -> bytes:
    hidden_bytes = base64.b64encode(secret_message.encode())
    return cover_ciphertext + b'||' + hidden_bytes

def extract_secret_from_cover(ciphertext_with_secret: bytes) -> str:
    try:
        cover, hidden = ciphertext_with_secret.split(b'||')
        return base64.b64decode(hidden).decode()
    except Exception as e:
        return f"No hidden message found. ({e})"
