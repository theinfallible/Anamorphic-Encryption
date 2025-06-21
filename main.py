from cover_crypto import aes_encrypt, aes_decrypt
from anamorphic_layer import embed_secret_into_cover, extract_secret_from_cover

# Normal encryption
message = b"This is a normal message"
cover_ciphertext = aes_encrypt(message)

# Embed secret
secret_message = "This is a secret hidden from dictator"
anamorphic_cipher = embed_secret_into_cover(cover_ciphertext, secret_message)

# Decrypting normal message
print("Decrypted cover message:", aes_decrypt(cover_ciphertext).decode())

# Extracting secret
print("Hidden message extracted:", extract_secret_from_cover(anamorphic_cipher))
