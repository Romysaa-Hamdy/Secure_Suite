import random, string
import hashlib

def generate_password():
    length = 12
    password = ""

    Random_letters = string.ascii_letters
    Numbers = string.digits
    Symbols = string.punctuation

    password += random.choice(Random_letters)
    password += random.choice(Numbers)
    password += random.choice(Symbols)

    Everything = Random_letters + Numbers + Symbols

    for i in range(length):
        password = "".join(random.sample(Everything, length))
        return password


def evaluate_password(password):
    booleanFlag1 = False
    booleanFlag2 = False
    booleanFlag3 = False
    booleanFlag4 = False

    Special_Syms = "!@#$%^&*()_+-=[]{|;':\",.<}>/?"

    for j in password:
        if len(password) >= 12:
            booleanFlag1 = True
        if j.isnumeric():
            booleanFlag2 = True
        if j.isupper():
            booleanFlag3 = True
        if any(j in Special_Syms for j in password):
            booleanFlag4 = True

    # Final decision
    if booleanFlag1 and booleanFlag2 and booleanFlag3 and booleanFlag4:
        return "Compliant"

    non_compliant_message = "Non-compliant.\nThe given password did not pass the following criteria:"
    if not booleanFlag1:
        non_compliant_message += "\n  - The password must be 12 or more characters"
    if not booleanFlag2:
        non_compliant_message += "\n  - The password must contain numbers"
    if not booleanFlag3:
        non_compliant_message += "\n  - The password must include uppercase letters"
    if not booleanFlag4:
        non_compliant_message += "\n  - The password is missing special characters (@!# etc.)"

    return non_compliant_message



def caesar_cipher(text, shift):
    result = ""

    for character in text:
        if character.isalpha():
            if character.isupper():
                result += chr((ord(character) - ord("A") + shift) % 26 + ord("A"))
            else:
                result += chr((ord(character) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += character
    return result


def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)



def calculate_md5(filename):
    hash_md5 = hashlib.new("md5")

    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

#main

def main():
    print("=== Security Tool ===")
    print("1) Generate Strong Password")
    print("2) Check Password Security")
    print("3) Encrypt File (Caesar Cipher)")
    print("4) Decrypt File (Caesar Cipher)")
    print("5) Calculate MD5 Hash of File")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Generated Password:", generate_password())

    elif choice == "2":
        pwd = input("Enter password: ")
        print(evaluate_password(pwd))

    elif choice == "3":
        filename = input("Enter file name to encrypt: ")
        shift = 3
        plaintext = open(filename, "r").read()
        encrypted = caesar_cipher(plaintext, shift)
        open("encrypted.txt", "w").write(encrypted)
        print("Encrypted text saved in encrypted.txt")

    elif choice == "4":
        filename = input("Enter file name to decrypt: ")
        shift = 3
        encrypted = open(filename, "r").read()
        decrypted = caesar_decipher(encrypted, shift)
        open("decrypted.txt", "w").write(decrypted)
        print("Decrypted text saved in decrypted.txt")

    elif choice == "5":
        filename = input("Enter file name: ")
        print("MD5 hash:", calculate_md5(filename))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
