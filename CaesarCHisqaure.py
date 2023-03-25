import string


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


def chi_squared(text):
    english_letter_frequencies = {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228,
        'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
        'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
        's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
        'y': 1.974, 'z': 0.074
    }

    text = text.lower()
    letter_counts = {char: text.count(char) for char in string.ascii_lowercase}
    total_chars = len(text)

    chi_squared_statistic = 0

    for letter, frequency in english_letter_frequencies.items():
        observed = letter_counts[letter]
        expected = total_chars * (frequency / 100)
        chi_squared_statistic += ((observed - expected) ** 2) / expected

    return chi_squared_statistic


def find_best_shift(ciphertext):
    min_chi_squared = float('inf')
    best_shift = None

    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        chi_squared_statistic = chi_squared(decrypted_text)

        if chi_squared_statistic < min_chi_squared:
            min_chi_squared = chi_squared_statistic
            best_shift = shift

    return best_shift


ciphertext = "Wklv lv qrz"
shift = find_best_shift(ciphertext)

plaintext = caesar_decrypt(ciphertext, shift)
print("Decrypted text:", plaintext)


