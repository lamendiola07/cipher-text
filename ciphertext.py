# Name:
# Year and Section:
# Course:
# Task: Program #3: Ciphered Text Using Vignere Cipher

import string

message_text = "THISISTHELASTTASKHOORDAY"
message_keycode = 'KNIGHTS'
message_text_ciphered = ""

character_count = 0

for c in message_text:
    if c in string.ascii_uppercase:
        offset = ord(message_keycode[character_count]) - ord('A')

        encryption_of_message_text = chr((ord(c) - ord('A') + offset) % 26 + ord('A'))
        message_text_ciphered = message_text_ciphered + encryption_of_message_text

        character_count = (character_count + 1) % len(message_keycode)
    
    else:
        message_text_ciphered = message_text_ciphered + c

print(pyfiglet.figlet_format('\nHere is the Plain Text Version of the Message:', font ='bulbhead'))
print(yellow(message_text,['bold','underlined']))

print(pyfiglet.figlet_format('\nHere is the Key used for the Message:', font ='bulbhead'))
print(yellow(message_keycode,['bold', 'underlined']))

print(pyfiglet.figlet_format('\nHere is the Ciphered Version of the Message:', font ='bulbhead'))
print(yellow(message_text_ciphered,['bold', 'underlined']))