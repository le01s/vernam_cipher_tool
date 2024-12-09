import random


def gen_pass(length):
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for _ in range(length)])
    return psw


def read_file(file):
    with open(file, 'r') as file_data:
        return file_data.read()


def vernam_encrypt(file):
    message = read_file(file)
    key = gen_pass(len(message))
    with open("key.txt", 'w') as key_data:
        key_data.write(key)
        print("Key saved!")
    if len(message) != len(key):
        raise ValueError("The length of the message and the key must match!")
    encrypted_message = ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))
    with open("encrypted.txt", 'w') as enc_file:
        enc_file.write(encrypted_message)
        print("Encrypted message saved!")

    return encrypted_message

def vernam_decrypt(encrypted_file, key_file):
    encrypted_message = read_file(encrypted_file)
    with open(key_file, 'r') as key_data:
        key = key_data.read()
    if len(encrypted_message) != len(key):
        raise ValueError("The length of the encrypted message and the key must match!")
    decrypted_message = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_message, key))
    with open("decrypted.txt", 'w') as dec_file:
        dec_file.write(decrypted_message)
        print("Decrypted message saved!")

    return decrypted_message


print(vernam_encrypt('1.txt'))
print(vernam_decrypt('encrypted.txt', 'key_2.txt'))