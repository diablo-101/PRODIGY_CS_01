def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == "encrypt":
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "decrypt":
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char

    return result

# Main program loop
if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift_value = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift_value, "encrypt")
            print(f"Encrypted message: {encrypted_message}")

        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift_value = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift_value, "decrypt")
            print(f"Decrypted message: {decrypted_message}")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
