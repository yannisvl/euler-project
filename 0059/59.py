with open('./0059/p059_cipher.txt', 'r') as f:
    cipher = f.read().split(',')
cipher = [int(code) for code in cipher]

import itertools

for key in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=3):
    message = ''
    for i in range(len(cipher)):
        message += chr(cipher[i] ^ ord(key[i % 3]))

    words = message.split()
    common_words = ['the', 'be', 'to', 'of', 'and', 'in', 'that', 'have', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'person', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']
    common_words_count = 0
    for word in words:
        if word.lower() in common_words:
            common_words_count += 1
    if common_words_count > 12: # Change the threshold as needed
        print('Key:', ''.join(key))
        print('Decrypted message:', message)
        print('Sum of ASCII values:', sum([ord(c) for c in message]))
        break
