from spellchecker import SpellChecker
from collections import Counter
import string

ENGLISH_FREQUENCY = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}


def calculate_frequency(text):
    total_chars = len(text)
    char_counts = Counter(text)
    return {char: (count / total_chars) * 100 for char, count in char_counts.items()}


def match_frequencies(cipher_frequencies):
    sorted_freq = sorted(ENGLISH_FREQUENCY.items(), key=lambda x: x[1], reverse=True)
    matched_freq = {}

    for cipher_char, freq in cipher_frequencies.items():
        min_diff = float('inf')
        matched_char = None

        for english_char, english_freq in sorted_freq:
            diff = abs(freq - english_freq)
            if diff < min_diff:
                min_diff = diff
                matched_char = english_char

        matched_freq[cipher_char] = matched_char

    return matched_freq


def decrypt(ciphertext, matched_freq):
    return ''.join(matched_freq.get(char, char) for char in ciphertext)


def is_word_valid(word):
    spell = SpellChecker()
    return word.lower() in spell.known([word.lower()])


def refine_decryption(ciphertext, decryption, matched_freq):
    words = decryption.split()
    for index, word in enumerate(words):
        if not is_word_valid(word):
            for i in range(len(word)):
                cipher_char = ciphertext[word.start() + i]
                substitution_options = [k for k, v in matched_freq.items() if v == word[i]]

                for option in substitution_options:
                    temp_decryption = decryption[:word.start() + i] + option + decryption[word.start() + i + 1:]
                    temp_word = temp_decryption.split()[index]

                    if is_word_valid(temp_word):
                        decryption = temp_decryption
                        matched_freq[cipher_char] = option
                        break
    return decryption


def decrypt_monoalphabetic_cipher(ciphertext):
    ciphertext = ciphertext.upper()
    cipher_frequencies = calculate_frequency(ciphertext)
    matched_freq = match_frequencies(cipher_frequencies)
    decryption = decrypt(ciphertext, matched_freq)
    final_decryption = refine_decryption(ciphertext, decryption, matched_freq)

    return final_decryption


ciphertext = "DJ DK C QLXDWI WF SDGDU PCX. XLRLU KQCSLKBDQK, KJXDHDET FXWZ C BDIILE RCKL, BCGL PWE JBLDX FDXKJ GDSJWXO CTCDEKJ JBL LGDU TCUCSJDS LZQDXL."
plaintext = decrypt_monoalphabetic_cipher(ciphertext)
print(plaintext)
