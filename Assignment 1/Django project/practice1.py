from datetime import date
from datetime import datetime
d, m, y = 12, 1, 2000
birth = datetime(y, m, d)
now = datetime.now()
today = datetime(datetime.now().year, birth.month, birth.day)
delta = (today-now)
print(delta.days)
print(delta)

age = now - birth
print(round(age.days/365.25))


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
     (birthDate.month, birthDate.day))

    return age


print(calculateAge(date(2000, 11, 11)), "years")

def only_int(a, b):
    if bool(type(a)==int and type(b)==int):
        print("True")
    else:
        print("False")    

 
only_int(1, 1)

def check_div(a):
    if a%3==0:
        print("True")
    else:
        print("False")

check_div(4)
def mid(stri):
    if len(stri)%2==0:
        print("False")
    else:
        print(stri[int(len(stri)/2 + 0.5 - 1)])

mid("aaaa")

class Person:
    fName = "Bhargav"
    lName = "Sonagara"
    def __str__(self):
        
        return f"{self.fName} {self.lName}"

bhargav = Person()
print(bhargav)