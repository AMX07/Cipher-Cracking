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

def find_shift(ciphertext):
    # A list of common English words to check against the decrypted text
    common_words = ["the", "and", "you", "that", "was", "for", "are", "with", "his", "they", "this", "have", "from", "one", "had", "word", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "each", "which", "she", "how", "their", "will", "other", "about", "out", "many", "then", "them", "these", "some", "her", "would", "make", "like", "him", "into", "time", "has", "look", "two", "more", "write", "go", "see", "number", "no", "way", "could", "people", "my", "than", "first", "been", "call", "who", "oil", "its", "now", "find", "long", "down", "day", "did", "get", "come", "made", "may", "part"]

    best_shift = None
    max_matches = 0

    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        words = decrypted_text.lower().split()
        matches = sum(1 for word in words if word in common_words)

        if matches > max_matches:
            max_matches = matches
            best_shift = shift

    return best_shift

ciphertext = "Wklv lv qrz"      #this is now
shift = find_shift(ciphertext)

plaintext = caesar_decrypt(ciphertext, shift)
print("Decrypted text:", plaintext)
