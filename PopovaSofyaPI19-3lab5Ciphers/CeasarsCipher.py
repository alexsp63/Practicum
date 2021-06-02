def encrypt(string_to_encrypt, k):
    return "".join([chr(ord(e)+k % 65536) for e in string_to_encrypt])

def decrypt(encrypted_string, k):
    try:
        return "".join([chr(ord(e)-k % 65536) for e in encrypted_string])
    except:
        return "\033[31m\nВ зашифрованном сообщении пробел - не самое частое значение!\033[0m"

def inp():
    input_string = input("\033[34mВведите строку для шифрования -> \033[0m")

    while True:
        try:
            key = int(input("\033[34m\nВведите целое положительное число - ключ -> \033[0m"))
            if key > 0:
                break
            else:
                continue
        except ValueError:
            print("\033[31m\nВы ввели не целое число, попробуйте снова!\033[0m")
            continue

    return input_string, key
    
if __name__ == "__main__":

    input_string, key = inp()

    encrypted_string = encrypt(input_string, key)
    print("\n\033[32mЗашифрованная строка -> \033[0m" + encrypted_string)
    print("\n\033[32mДешифрованная строка -> \033[0m" + decrypt(encrypted_string, key))