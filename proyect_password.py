import random
import string


class Password:
    def __init__(self, long, password):
        self.long = long
        self.password = password
        self.cont_may = 0
        self.cont_min = 0
        self.cont_num = 0

    def is_hard(self):
        for e in self.password:
            if ord(e) >= 65 and ord(e) <= 90:
                self.cont_may += 1
            elif ord(e) >= 97 and ord(e) <= 122:
                self.cont_min += 1
            elif isinstance(ord(e), int):
                self.cont_num += 1
        if self.cont_may > 2:
            if self.cont_min > 1:
                if self.cont_num > 5:
                    return "es fuerte"
                return "es debil"
            return "es debil"
        return "es debil"

class Random_chr(Password):
    def __init__(self, long):
        self.long = long
        self.num = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    def char(self):
        mayus = string.ascii_letters
        for i in range(0, 9):
            mayus += str(i)
        pas_chr = ""
        for e in range(self.long):
            pas_chr += random.choice(mayus)
        return pas_chr

longt = int(input("ingrese la longitud de la contrasena, de 8 en adelante: "))

passw = Random_chr(longt)
first_password = Password(longt, passw.char())

print(first_password.is_hard())
print(passw.char())