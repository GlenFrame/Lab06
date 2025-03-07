from xml.sax.saxutils import escape

key = 'FONDUE'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"

def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print('|   ', end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i]}", end=' ')
    print('|')
    print(f"{'|---'*(alpha_len+1)}|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                c = alphabet[(i + shift) % alpha_len]
                print(f"| {c}", end=' ')
                print(f"| {c}", end=' ')
            else:
                print(f"| {c}", end=' ')
        print("|")

def letter_to_index(letter, alphabet):
    return alphabet.lower().index(letter.lower())

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return ((letter_to_index(key_letter, alphabet) +
             letter_to_index(plaintext_letter, alphabet)) % len(alphabet))

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif(c.upper() in alphabet):
            cipher_text += index_to_letter(vigenere_index(key[counter%len(key)], c, alphabet), alphabet)
            counter += 1
    return cipher_text

def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    return index_to_letter((((letter_to_index(cypher_letter, alphabet))
                            - letter_to_index(key_letter, alphabet)) % len(alphabet)), alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
    plaintext = ''
    counter = 0
    for c in cipher_text:
        if c == ' ':
            plaintext += ' '
        elif(c.upper() in alphabet):
            plaintext += undo_vigenere_index(key[counter%len(key)], c, alphabet)
            counter += 1
    return plaintext

def user_interface():
    print(f'{BOLD}Vigenère Cipher Menu:{RESET}')
    print(f"1:{RED} Encrypt{RESET}")
    print(f"2:{GREEN} Decrypt{RESET}")
    print(f"3:{BLUE} Exit {RESET}")
    encrypt_decrypt = input(f'{BOLD}Select an option')
    if encrypt_decrypt == '1':
        plaint_text = input(f'{BOLD}Enter plain text to encrypt')
        encrypted = encrypt_vigenere(key, plaint_text, alphabet)
        print(f'Encrypted text:{RED}', encrypted, f'{RESET}')
        user_interface()
    elif encrypt_decrypt == '2':
        cipher_text = input(f'{BOLD}Enter cipher text to decrypt')
        decrypted = decrypt_vigenere(key, cipher_text, alphabet)
        print(f'Decrypted text:{GREEN}', decrypted, f'{RESET}')
        user_interface()
    elif encrypt_decrypt == '3':
        print(f'{BOLD}Bye Bye')
    else:
        print(f'{BOLD} {RED}Oopsie you made a typo{RESET}')
        user_interface()



message = 'Very important secret message'
cipher_text = encrypt_vigenere(key, message, alphabet)

user_interface()

#print(decrypt_vigenere(key, cipher_text, alphabet))
#print(encrypt_vigenere(key, message, alphabet))

#print(undo_vigenere_index('J', 'L', alphabet))
#print(encrypt_vigenere(key, message, alphabet))
#print(vigenere_index('B', 'H', alphabet))
#print(letter_to_index("Z", alphabet))
#print(index_to_letter(25, alphabet))
#vigenere_sq(alphabet)