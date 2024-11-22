def caesar_decrypt(shift, text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += new_char
        else:
            decrypted_text += char 
    return decrypted_text

def decrypt_cipher(input_cipher):
    parts = input_cipher.split()  
    result = []
    for part in parts:
        shift = int(part[0]) 
        cipher_text = part[1:] 
        result.append(caesar_decrypt(shift, cipher_text))
    return " ".join(result)

if __name__ == "__main__":
    cipher_input = input("Enter cipher: ")
    decrypted_message = decrypt_cipher(cipher_input)
    print("Message =", decrypted_message)
