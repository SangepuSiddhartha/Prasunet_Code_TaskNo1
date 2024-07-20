def caesar_cipher(text, shift, action='encrypt'):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            # Determine the base (uppercase or lowercase ASCII value)
            base = ord('A') if char.isupper() else ord('a')
            # Compute the shifted position
            shifted = (ord(char) - base + shift) % 26 + base
            # Convert ASCII value back to character
            encrypted_text.append(chr(shifted))
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)


def main():
    print("Welcome to the Caesar Cipher program!")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (an integer): "))
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (an integer): "))
            decrypted_message = caesar_cipher(message, -shift, action='decrypt')
            print(f"Decrypted message: {decrypted_message}")
        
        elif choice == '3':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
