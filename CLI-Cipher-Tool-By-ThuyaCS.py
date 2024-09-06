# Made by ThuyaCS

def encrypt_CC(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def decrypt(ciphertext, shift):
    return encrypt_CC(ciphertext, -shift)

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    
    encrypted_text = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt_VC(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    decrypted_text = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text

while True:
    try:
        enc_choice = input("\n1. Caesar Cipher\n2. Vigenère cipher\n3. Exit\n\n>> ")
        
        if enc_choice == "3":
            print("Exiting...")
            break
        
        if enc_choice == "1" or enc_choice.lower() == "caesar cipher":
            text = str(input("\nEnter text $ "))
            shift = int(input("\nShifts $ "))
            en_or_de_both = str(input("\nEncrypt or Decrypt or both? (en/de/both) $ "))
            
            if en_or_de_both == 'en':
                encrypted = encrypt_CC(text, shift)
                print(f"\nEncrypted: {encrypted}")
            elif en_or_de_both == 'de' or en_or_de_both == 'decrypt':
                decrypted = decrypt(text, shift)
                print(f"\nDecrypted: {decrypted}\n")
            elif en_or_de_both == 'both':
                encrypted = encrypt_CC(text, shift)
                print(f"\nEncrypted: {encrypted}")
                decrypted = decrypt(encrypted, shift)
                print(f"\nDecrypted: {decrypted}\n")
            else:
                print("\nInvalid option. Please enter 'en', 'de', or 'both'.")
        
        elif enc_choice == "2" or enc_choice.lower() in ["vigenere cipher", "vigenère cipher"]:
            text = str(input("\nEnter text $ "))
            key = str(input("\nEnter key $ "))
            en_or_de_both = str(input("\nEncrypt or Decrypt or both? (en/de/both) $ "))
            
            if en_or_de_both == 'en':
                encrypted = vigenere_encrypt(text, key)
                print(f"\nEncrypted: {encrypted}")
            elif en_or_de_both == 'de' or en_or_de_both == 'decrypt':
                decrypted = decrypt_VC(text, key)
                print(f"\nDecrypted: {decrypted}\n")
            elif en_or_de_both == 'both':
                encrypted = vigenere_encrypt(text, key)
                print(f"\nEncrypted: {encrypted}")
                decrypted = decrypt_VC(encrypted, key)
                print(f"\nDecrypted: {decrypted}\n")
            else:
                print("\nInvalid option. Please enter 'en', 'de', or 'both'.")
        else:
            print("\nInvalid choice. Please select a valid encryption method.")
    except ValueError as ve:
        print(f"\nError: Invalid input. {ve}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
