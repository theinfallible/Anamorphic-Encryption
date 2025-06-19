# Anamorphic Encryption: Private Communication against a Dictator

This is a prototype implementation inspired by the research paper [Anamorphic Encryption (ePrint 2022/639)](https://eprint.iacr.org/2022/639).

## 📌 Features
- AES-based cover encryption
- Hides anamorphic message inside cover ciphertext
- Can extract hidden message only if special decoder is used

## 🧪 How to Run
```bash
pip install -r requirements.txt
python main.py

Sample RUn:
Decrypted cover message: This is a normal message
Hidden message extracted: This is a secret hidden from dictator
