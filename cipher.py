# add your code here

def create_cipher_dict(shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_dict = {}
    for i in range(len(alphabet)):
        cipher_dict[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]
    return cipher_dict

def encrypt_text(text, cipher_dict):
    encrypted_text = ''
    for char in text:
        if char.lower() in cipher_dict:
            if char.isupper():
                encrypted_text += cipher_dict[char.lower()].upper()
            else:
                encrypted_text += cipher_dict[char]
        else:
            encrypted_text += char
    return encrypted_text

def main():
    shift = 5
    cipher_dict = create_cipher_dict(shift)
    user_input = input("Enter the text to encrypt: ")
    encrypted_text = encrypt_text(user_input, cipher_dict)
    print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()