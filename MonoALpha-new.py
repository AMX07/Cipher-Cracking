from collections import Counter
import string

def frequency_analysis(cipher_text):
    letters = string.ascii_lowercase
    english_letter_freq = {
        'a': 8.12, 'b': 1.49, 'c': 2.71, 'd': 4.32, 'e': 12.02,
        'f': 2.30, 'g': 2.03, 'h': 5.92, 'i': 7.31, 'j': 0.10,
        'k': 0.69, 'l': 3.98, 'm': 2.61, 'n': 6.95, 'o': 7.68,
        'p': 1.82, 'q': 0.11, 'r': 6.02, 's': 6.28, 't': 9.10,
        'u': 2.88, 'v': 1.11, 'w': 2.09, 'x': 0.17, 'y': 2.11, 'z': 0.07,
    }
    cipher_text = cipher_text.lower()
    char_count = Counter(c for c in cipher_text if c.isalpha())
    total_chars = sum(char_count.values())

    cipher_freq = {
        char: (count / total_chars) * 100 for char, count in char_count.items()
    }

    sorted_english_freq = sorted(english_letter_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_cipher_freq = sorted(cipher_freq.items(), key=lambda x: x[1], reverse=True)

    substitution_table = {}
    for (plain_char, _), (cipher_char, _) in zip(sorted_english_freq, sorted_cipher_freq):
        substitution_table[cipher_char] = plain_char

    return substitution_table

def decipher(cipher_text, substitution_table):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            is_upper = char.isupper()
            original_char = char.lower()
            plain_char = substitution_table.get(original_char, original_char)
            plain_text += plain_char.upper() if is_upper else plain_char
        else:
            plain_text += char
    return plain_text

cipher_text = "DJ DK C QLXDWI WF SDGDU PCX. XLRLU KQCSLKBDQK, KJXDHDET FXWZ C BDIILE RCKL, BCGL PWE JBLDX FDXKJ GDSJWXO CTCDEKJ JBL LGDU TCUCSJDS LZQDXL. IYXDET JBL RCJJUL, XLRLU KQDLK ZCECTLI JW KJLCU KLSXLJ QUCEK JW JBL LZQDXL’K YUJDZCJL PLCQWE, JBL ILCJB KJCX, CE CXZWXLI KQCSL KJCJDWE PDJB LEWYTB QWPLX JW ILKJXWO CE LEJDXL QUCELJ. QYXKYLI RO JBL LZQDXL’K KDEDKJLX CTLEJK, QXDESLKK ULDC XCSLK BWZL CRWCXI BLX KJCXKBDQ, SYKJWIDCE WF JBL KJWULE QUCEK JBCJ SCE KCGL BLX QLWQUL CEI XLKJWXL FXLLIWZ JW JBL TCUCVO."

substitution_table = frequency_analysis(cipher_text)
plain_text = decipher(cipher_text, substitution_table)
print(plain_text)
