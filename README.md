# LFSR Cryptanalysis

This Python project implements a cryptographic analysis using a Linear Feedback Shift Register (LFSR). The project includes functions to encode and decode text, perform XOR operations, generate keystreams using LFSR, and brute-force search for LFSR seeds to decrypt a given ciphertext.
Given the LFSR with feedback polynomial $x^{10} + x^9 + x^7 + x^6 + 1$ and the encrypted message `i!))iszwykqnf cyc!?secnncvch`, the goal is to find the original plaintext message. Feedback polynomial and encrypted message can be changed to your liking

## Features
- **Character to Bits Conversion**: Maps characters to their corresponding 5-bit binary representation.
- **Bits to Character Conversion**: Maps 5-bit binary strings back to their corresponding characters.
- **Text Encoding/Decoding**: Converts text to a binary string and vice versa.
- **XOR Operations**: Performs bitwise XOR between two binary strings.
- **LFSR Keystream Generation**: Generates a keystream using an LFSR with a given seed and feedback polynomial.
- **Brute-Force LFSR**: Attempts to find the correct LFSR seed by brute-forcing all possible seeds and checking the decrypted text.

## Functions

### `list_to_string(l)`
Converts a list of integers to a concatenated string.
- **Parameters**: `l` (list) - The list to be converted.
- **Returns**: (str) - The concatenated string.

### `text_enc(text)`
Encodes a given text message to a binary string using a predefined character to binary mapping.
- **Parameters**: `text` (str) - The text message to be encoded.
- **Returns**: (str) - The resulting binary string.

### `text_dec(binary_string)`
Decodes a binary string back to the original text message using a predefined binary to character mapping.
- **Parameters**: `binary_string` (str) - The binary string to be decoded.
- **Returns**: (str) - The resulting text message.

### `string_xor(btext, key)`
Performs bitwise XOR between two binary strings.
- **Parameters**: 
  - `btext` (str) - The binary string representing the text.
  - `key` (str) - The binary string representing the key.
- **Returns**: (str) - The resulting binary string after XOR operation.

### `sumxor(l)`
Calculates the XOR sum of a list of integers.
- **Parameters**: `l` (list) - The list of integers.
- **Returns**: (int) - The resulting XOR sum.

### `lfsr(seed, feedback, bits, flag)`
Generates a keystream using an LFSR with the given seed and feedback polynomial.
- **Parameters**: 
  - `seed` (list) - The initial seed for the LFSR.
  - `feedback` (list) - The feedback polynomial coefficients.
  - `bits` (int) - The number of bits in the generated keystream.
  - `flag` (int) - Flag to print intermediate states (0 for printing, 1 for silent).
- **Returns**: (list) - The generated keystream.

### `brute_force_lfsr(streambits)`
Attempts to find the correct LFSR seed by brute-forcing all possible 10-bit seeds and checking the decrypted text.
- **Parameters**: `streambits` (str) - The binary string of the ciphertext to be decrypted.
- **Returns**: None
