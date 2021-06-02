from VernamCiper import *
import random

def in_bytes(message):
    return "".join([bin(ord(el))[2::] for el in message])

if __name__ == "__main__":


    message = input("Введите сообщение -> ")
    bytes_mess = in_bytes(message)
    bts = len(bytes_mess)

    #разобью на 3 блока
    if (bts % 3 == 0):
        len_of_one = bts // 3
    elif (bts % 3 == 1):
        len_of_one = (bts + 2) // 3
    else:
        len_of_one = (bts + 1) // 3
    
    blocks = [bytes_mess[i:i + len_of_one] for i in range(0, bts, len_of_one)]

    if len(blocks[-1]) < len_of_one:
        blocks[-1] += "0"*(len_of_one-len(blocks[-1]))

    IV = "".join([chr(random.randint(0, 65536)) for i in range(len_of_one)])
    
    #сформировала три одинаковых блока

    Ci_1 = IV

    for block in blocks:

        key = input("\nВведите секретный ключ -> ")
        
        open_text = chr(int(block, base=2)) 

        if len(key) < len(open_text):
            key += chr(0)*(len(open_text)-len(key))
        else:
            open_text += chr(0)*(len(key)-len(open_text))

        print("\nКлюч: " + key)
        print("Открытый текст: " + open_text)

        C = "%s" % Ci_1 #копирую строку

        #шифрую
        Ci_1 = one_time_pad_encrypt(one_time_pad_encrypt(block, Ci_1), key)
        print("\nЗашифрованный текст: " + Ci_1)

    print("\n***Итог шифрования: " + Ci_1)



        
