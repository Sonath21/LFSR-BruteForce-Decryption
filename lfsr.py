from collections import deque
from itertools import product

aDict = dict(zip(
    'abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111',
     '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111',
     '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111',
     '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111',
     '00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111',
     '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111',
     '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111',
     '11000', '11001']
))


def list_to_string(l):
    return ''.join(str(e) for e in l)


def text_enc(text):
    text = text[::-1]
    length = len(text)
    coded_text = ''
    for i in range(length):
        coded_text = aDict[text[i]] + coded_text
    return coded_text.lower()


def text_dec(binary_string):
    length = len(binary_string)
    inv_map = {v: k for k, v in aDict.items()}
    decoded_text = ''
    for i in range(0, length, 5):
        decoded_text = inv_map[binary_string[i:i + 5]] + decoded_text
    decoded_text = decoded_text[::-1]
    return decoded_text.lower()


def string_xor(btext, key):
    cipher = []
    if len(btext) != len(key):
        print("Key and message must have the same lengths!")
        return 0
    for i in range(len(btext)):
        cipher.append(int(btext[i]) ^ int(key[i]))
    return ''.join(str(e) for e in cipher)


def sumxor(l):
    r = 0
    for v in l:
        r = r ^ v
    return r


def lfsr(seed, feedback, bits, flag):
    index_of_ones = []
    feedback_new = []
    for i in range(len(feedback)):
        if feedback[i] == 1:
            index_of_ones.append(i)
    seed = deque(seed)
    output = []
    if flag == 0:
        print('Initial seed:', list(seed))
    for i in range(bits):
        xor = sum(seed[j] for j in index_of_ones) % 2
        output.append(seed.pop())
        seed.appendleft(xor)
        if flag == 0:
            print('State', i + 1, ':', list(seed))
    return output


def brute_force_lfsr(streambits):
    n = 10
    feedback = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
    count = 0
    for current_seed in product([0, 1], repeat=n):
        count += 1
        seed = list(current_seed)
        O = lfsr(seed, feedback, len(streambits), 1)
        keystream = list_to_string(O)
        decrypted_binary = string_xor(text_enc("i!))aiszwykqnfcyc!?secnncvch"), keystream)
        decrypted_text = text_dec(decrypted_binary)
        print(decrypted_text, seed)

        if count == 812:
            print(f"Seed found {seed} on iteration {count}: {decrypted_text}")
            break


encoded_text = "i!))aiszwykqnfcyc!?secnncvch"
streambits = text_enc("i!))aiszwykqnfcyc!?secnncvch")

brute_force_lfsr(streambits)
