text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

        if char == ' ':
            encrypted_text += char

        else:
            # stores the index of each letter in a variable named index
            index = alphabet.find(char)
            # shifts letter by specified offset and wraps around if index goes beyond the length of alphabet
            new_index = (index + offset) % len(alphabet)
            # stores the shifted letters into a variable named encrypted_text
            encrypted_text += alphabet[new_index]

    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)   
