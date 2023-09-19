import secrets
import string

letters_min = 'abcdefghijklmopqrstuvwxyz'
letters_max = 'ABCDEFGHIJKLMOPQRSTUVWXYZ'


def Create_password(longitud):
    letters = string.ascii_letters + string.digits + string.punctuation
    paswword = ''
    for i in range(longitud):
        paswword += secrets.choice(letters)
    return  paswword

resultado = Create_password(12)
print(resultado)