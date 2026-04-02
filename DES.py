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
