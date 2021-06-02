def one_time_pad_encrypt(key, message):

    return "".join([chr(ord(key[i]) ^ ord(message[i])) for i in range(len(message))])

def one_time_pad_decrypt(key, encrypted_message):

    return one_time_pad_encrypt(key, encrypted_message)

if __name__ == "__main__":

    while True:
        message = input("\nВведите сообщение для шифрования -> ")
        key = input("\nВведите ключ для шифрования (он должен быть такого же размера, как сообщение) -> ")
        if len(message) == len(key):
            encrypted_message = one_time_pad_encrypt(key, message)
            break
        else:
            print("\nДлина ключа не совпадает с длиной сообщения, что противоречит условию, попробуйте снова!")
            continue

    print("\n***Закодированное сообщение:\n" + encrypted_message + "\n")

    print("Раскодированное сообщение:\n" + one_time_pad_decrypt(key, encrypted_message))