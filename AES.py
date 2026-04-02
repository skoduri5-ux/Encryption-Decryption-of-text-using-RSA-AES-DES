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
