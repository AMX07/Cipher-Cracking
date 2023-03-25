from collections import Counter
import string

def keyword_monoalphabetic_decrypt(ciphertext, substitution):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            new_char = substitution[char]
            plaintext += new_char
        else:
            plaintext += char

    return plaintext

def find_substitution(ciphertext):
    english_letter_frequencies = {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
        'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
        'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
        's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
        'y': 1.974, 'z': 0.074
    }

    ciphertext = ciphertext.lower()
    letter_counts = Counter(ciphertext)
    total_chars = sum(letter_counts[char] for char in string.ascii_lowercase)

    if total_chars == 0:
        return None

    frequencies = {char: (letter_counts[char] / total_chars) * 100 for char in string.ascii_lowercase}
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    sorted_english_frequencies = sorted(english_letter_frequencies.items(), key=lambda x: x[1], reverse=True)

    substitution = {}

    for i in range(len(sorted_frequencies)):
        substitution[sorted_frequencies[i][0]] = sorted_english_frequencies[i][0]
        substitution[sorted_frequencies[i][0].upper()] = sorted_english_frequencies[i][0].upper()

    return substitution

ciphertext = "rEgrt eqf yofr qshiqwtzoeqs lxwlzozxzogfl dqrt zg q ztbz wn qfqsnmofu stzztk yktjxtfeotl."
substitution = find_substitution(ciphertext)

plaintext = keyword_monoalphabetic_decrypt(ciphertext, substitution)
print("Decrypted text:", plaintext)
