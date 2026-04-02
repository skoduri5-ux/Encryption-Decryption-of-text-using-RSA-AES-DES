from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from cryptography.hazmat.primitives.asymmetric import rsa, padding as rsa_padding
from cryptography.hazmat.primitives import hashes

def aes_encrypt_decrypt(message):
    key = get_random_bytes(16)  # AES-128
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    print("\n🔐 AES Encrypted (Hex):", (iv + ciphertext).hex())

    # Decrypt
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)
    print("🔓 AES Decrypted:", decrypted.decode())

def des_encrypt_decrypt(message):
    key = get_random_bytes(8)  # DES uses 8-byte key
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode(), DES.block_size))
    print("\n🔐 DES Encrypted (Hex):", (iv + ciphertext).hex())

    # Decrypt
    cipher_dec = DES.new(key, DES.MODE_CBC, iv)
    decrypted = unpad(cipher_dec.decrypt(ciphertext), DES.block_size)
    print("🔓 DES Decrypted:", decrypted.decode())

def rsa_encrypt_decrypt(message):
    # Generate RSA key pair
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Encrypt
    ciphertext = public_key.encrypt(
        message.encode(),
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\n🔐 RSA Encrypted (Hex):", ciphertext.hex())

    # Decrypt
    decrypted = private_key.decrypt(
        ciphertext,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("🔓 RSA Decrypted:", decrypted.decode())

def main():
    print("💡 Choose Encryption Method:")
    print("1. AES")
    print("2. DES")
    print("3. RSA")

    choice = input("Enter your choice (1/2/3): ")
    message = input("Enter the message to encrypt: ")

    if choice == '1':
        aes_encrypt_decrypt(message)
    elif choice == '2':
        des_encrypt_decrypt(message)
    elif choice == '3':
        rsa_encrypt_decrypt(message)
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
