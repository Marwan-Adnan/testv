alphabet = 'abcdefghijklmnopqrstuvwxyz '
letter_to_index=dict(zip(alphabet,range(len(alphabet))))
index_to_latter=dict(zip(range(len(alphabet)),alphabet))
def encrypt(plaintext,key):
    encrypted =''
    # spilt the message to the length of the key
    split_message = [plaintext[i:i + len(key)] for i in range(0, len(plaintext),len(key))] # (start , end , step)
    # want to convert the message to index and add the key (mod 26)
    for each_split in split_message:
        i = 0
        for letter in each_split:
            number= (letter_to_index[letter] + letter_to_index[key[i]])%len(alphabet)
            encrypted += index_to_latter[number]
            i += 1
    return encrypted
def decrypt(cipher,key):
    decrypted = ''
    #split the cipher to the length of the key
    split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]  # (start , end , step)
    # convert cipher to index and subtract key (mod 26)
    for each_split in split_cipher:
        i = 0
        for letter in each_split:
            number= (letter_to_index[letter] - letter_to_index[key[i]])%len(alphabet)
            decrypted += index_to_latter[number]
            i += 1
    return decrypted
    pass
def main():
  plaintext = 'we are discovered save your self'
  key = 'deceptive'
  encrypted_plaintext = encrypt(plaintext,key)
  decrypted_plaintext = decrypt(encrypted_plaintext, key)
  print('plaintext is: '+plaintext)
  print('Encrypted message is: '+encrypted_plaintext)
  print('decrypted message is: '+decrypted_plaintext)
main()