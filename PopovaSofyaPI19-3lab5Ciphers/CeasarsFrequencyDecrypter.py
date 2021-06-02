from CeasarsCipher import *

# в задании предлагается предполагать, что самый частый символ - это пробел

def decrypt_encrypted(encrypted_string):

    #посмотрю по самым встречающимя значениям
    counts = sorted([(encrypted_string.count(letter), letter) for letter in set(encrypted_string)], reverse=True)
    
    freq = [el[1] for el in counts if el[0] == counts[0][0]] #значения, встречающиеся чаще всего
    #теперь предполагаем, что каждое из этих значений - пробел
    print("\nДешифровка при предположении, что пробел - один из самых частых символов:\n")
    for f in freq:
        if ord(f) >= ord(" "):
            key = ord(f)-ord(" ")
        else:
            key = 65536 - (ord(" ") - ord(f))
    print(decrypt(encrypted_string, key))
    

if __name__ == "__main__":

    input_string, key = inp()

    encrypted_string = encrypt(input_string, key)
    print("\n\033[32mЗашифрованная строка -> \033[0m" + encrypted_string)

    decrypted = decrypt_encrypted(encrypted_string)