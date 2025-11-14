import random
for i in range(10):
    print(random.choice('abcdefg'), end="")

#%% Task 1 - testing the menu
print("Caesar Cipher Encoder & Decoder")
print("-------------------------------")
print("Menu: 1. encode; 2. decode; e. exit.")

choice = input("Your choice: ")

while choice != 'e':
    if choice == '1':
        print("encode")
    elif choice == '2':
        print("decode")

    print("Menu: 1. encode; 2. decode; e. exit.")
    choice = input("Your choice: ")

#%% Encoding a single message

plaintext = input("Enter a message to encode: ")
plaintext = plaintext.upper()

ciphertext = ""

for p in plaintext:
    # Get ASCII value.
    p = ord(p)
    # Minus 65 to get the corresponding value between 0 and 25.
    p = p - ord('A')
    # Encode using the Caesar Cipher.
    c = (p + 1) % 26
    # Add back 65 to get the corresponding value between 65 and 90.
    c = c + ord('A')
    # Convert this number back to the corresponding ASCII character.
    c = chr(c)
    ciphertext += c

print("Encoded:", ciphertext)

#%% Putting it together
print("Caesar Cipher Encoder & Decoder")
print("-------------------------------")
print("Menu: 1. encode; 2. decode; e. exit.")

choice = input("Your choice: ")

while choice != 'e':
    if choice == '1':
        plaintext = input("Enter a message to encode: ")
        plaintext = plaintext.upper()
        ciphertext = ""

        for p in plaintext:
            p = ord(p)
            p = p - ord('A')
            c = (p + 1) % 26
            c = c + ord('A')
            c = chr(c)
            ciphertext += c

        print("Encoded:", ciphertext)
    elif choice == '2':
        ciphertext = input("Enter a message to decode: ").upper()
        plaintext = ""

        for c in ciphertext:
            c = ord(c) - ord('A')
            p = (c - 1) % 26
            p = p + ord('A')
            p = chr(p)
            plaintext += p

        print("Decoded:", plaintext)
    print("Menu: 1. encode; 2. decode; e. exit.")

    choice = input("Your choice: ")

#%% Task 2
import random

print("""Random Password Generator
-------------------------""")
choice = input("Enter 'g' to generate a password or 'e' to exit: ")

while choice != 'e':
    length = input("Enter length: ")
    length = int(length)

    uppercase = input("Use uppercase characters? [Y/n] ").upper()
    lowercase = input("Use lowercase characters? [Y/n] ").upper()
    numbers = input("Use numbers? [Y/n] ").upper()
    special = input("Use special characters? [Y/n] ").upper()

    charset = ""
    if uppercase == 'Y' or uppercase == '':
        for i in range(65, 91):
            charset += chr(i)
    if lowercase == 'Y' or lowercase == '':
        for i in range(97, 123):
            charset += chr(i)
    if numbers == 'Y' or numbers == '':
        for i in range(48, 58):
            charset += chr(i)
    if special == 'Y' or special == '':
        for i in range(33, 48):
            charset += chr(i)
        for i in range(58, 65):
            charset += chr(i)
        for i in range(91, 97):
            charset += chr(i)
        for i in range(123, 127):
            charset += chr(i)

    password = ""
    for i in range(length):
        password += random.choice(charset)

    print("Generated password: ", password)

    choice = input("Enter 'g' to generate a password or 'e' to exit: ")

print("Goodbye.")
