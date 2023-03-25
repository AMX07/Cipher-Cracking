def caesar_decrypt(ciphertext, shift):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            plaintext += new_char
        else:
            plaintext += char

    return plaintext

ciphertext = "Kl wklv lv dqvk"
shift = 3

plaintext = caesar_decrypt(ciphertext, shift)
print("Decrypted text:", plaintext)
