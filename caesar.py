import string
alphabet = "abcdefghijklmnopqrstuvwxyz" 

def alphabet_position(letter):    
    letters = letter.lower()
    if letters in alphabet:
        position = alphabet.find(letters)
    return position

def rotate_character(char,rot):
    rotated = ''
    if char.isalpha() == True:
        orig = alphabet_position(char)
        new = (orig + rot) % 26
        new_letter = alphabet[new]
        if char.islower() == True:
            rotated = rotated + new_letter.lower()
        if char.islower() == False:
            rotated = rotated + new_letter.upper()
    else:
        rotated = rotated + char
    return rotated

def encrypt(text,rot):
    encrypted = ''
    for char in text:
        encrypted = encrypted + rotate_character(char,rot)

    return encrypted