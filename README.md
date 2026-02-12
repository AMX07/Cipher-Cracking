# Cipher Cracking

A collection of Python scripts for decrypting classical ciphers using various cryptanalysis techniques.

## Scripts

### Caesar Cipher

| Script | Technique | Description |
|--------|-----------|-------------|
| `Caesar.py` | Known shift | Decrypts a Caesar cipher when the shift value is already known. |
| `BruteForce_Caesar.py` | Dictionary matching | Tries all 25 possible shifts and picks the one that produces the most common English words. |
| `CaesarCHisqaure.py` | Chi-squared analysis | Uses chi-squared statistical testing against standard English letter frequencies to find the most likely shift. |

### Monoalphabetic Substitution Cipher

| Script | Technique | Description |
|--------|-----------|-------------|
| `MonoALpha-new.py` | Frequency analysis | Cracks a monoalphabetic substitution cipher by mapping the most frequent ciphertext letters to the most frequent English letters. |
| `MonoAlphaKey.py` | Frequency analysis | Similar approach — builds a full substitution table (upper and lowercase) from letter frequency rankings. |

### Atbash Cipher

| Script | Technique | Description |
|--------|-----------|-------------|
| `atbash` | Direct reversal | Decrypts the Atbash cipher, where each letter is mapped to its reverse in the alphabet (A↔Z, B↔Y, etc.). |

## Usage

Each script can be run directly with Python 3. Edit the `ciphertext` variable inside the script to supply your own encrypted text.

```bash
python3 Caesar.py
python3 BruteForce_Caesar.py
python3 CaesarCHisqaure.py
python3 MonoALpha-new.py
python3 MonoAlphaKey.py
python3 atbash
```

## Requirements

Python 3 — no external dependencies. All scripts use only the standard library (`collections`, `string`).
