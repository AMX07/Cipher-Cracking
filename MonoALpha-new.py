import itertools
import string
from collections import Counter
from operator import itemgetter

def frequency_analysis(cipher_text):
    freq = Counter()
    cipher_text = cipher_text.lower()

    for char in cipher_text:
        if char.isalpha():
            freq[char] += 1

    sorted_freq = sorted(freq.items(), key=itemgetter(1), reverse=True)
    return sorted_freq

def create_decryption_map_from_guess(known_cipher_chars, known_plain_chars):
    key_map = {}
    for cc, pc in zip(known_cipher_chars, known_plain_chars):
        key_map[cc] = pc
    return key_map

def decrypt_with_frequency_analysis(cipher_text):
    eng_freq = "etaoinshrdlcumwfgypbvkjxqz"
    cipher_freq = frequency_analysis(cipher_text)
    cipher_freq_chars = "".join([char for char, freq in cipher_freq])

    decryption_map = create_decryption_map_from_guess(cipher_freq_chars, eng_freq)
    decrypted_text = ''

    for char in cipher_text:
        if char.isalpha():
            is_upper = char.isupper()
            decrypted_char = decryption_map.get(char.lower(), '?')
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

# Example usage
cipher_text = "XKWTI ZQ GVTIA!"
plain_text_guess = decrypt_with_frequency_analysis(cipher_text)
print(plain_text_guess)
