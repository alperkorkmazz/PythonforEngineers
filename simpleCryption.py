"""
crypt the sentence 'Hi Friend. How are you 07? I am fine.' using the key 8
write the crypted and decrypted forms on screen
"""
message='Hi Friend. How are you 07? I am fine.'
key=308
encrypted=""
for x in message:
    encrypted=encrypted+chr(ord(x)+8)
print(encrypted)
decrypted=""
for x in encrypted:
    decrypted=decrypted+chr(ord(x)-8)
print(decrypted)
